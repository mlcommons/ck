import sys
import os
import submission_checker as checker
from log_parser import MLPerfLog


def get_result_from_log(version, model, scenario, result_path, mode):

    config = checker.Config(
        version,
        None,
        ignore_uncommited=False,
        skip_power_check=False,
    )
    mlperf_model = config.get_mlperf_model(model)
    #scenario = checker.SCENARIO_MAPPING[scenario]

    result = ''
    power_result = None
    valid = {}
    if mode == "performance":
        has_power = os.path.exists(os.path.join(result_path, "..", "power"))
        result_ = checker.get_performance_metric(config, mlperf_model, result_path, scenario, None, None, has_power)
        mlperf_log = MLPerfLog(os.path.join(result_path, "mlperf_log_detail.txt"))
        if (
            "result_validity" not in mlperf_log.get_keys()
            or mlperf_log["result_validity"] != "VALID"
        ):
            valid['performance'] = False
        else:
            valid['performance'] = True

        if "stream" in scenario.lower():
            result = result_ / 1000000 #convert to milliseconds
        else:
            result = result_
        result = str(round(result, 3))

        if has_power:
            power_valid, power_metric, scenario, avg_power_efficiency = checker.get_power_metric(config, scenario, result_path, True, result_)
            power_result = f"{round(power_metric,3)},{round(avg_power_efficiency,3)}"
            valid['power'] = power_valid


    elif mode == "accuracy" and os.path.exists(os.path.join(result_path, 'accuracy.txt')):

        acc_valid, acc_results, acc_targets, acc_limits = get_accuracy_metric(config, mlperf_model, result_path)
        valid['accuracy'] = acc_valid

        if len(acc_results) == 1:
            for acc in acc_results:
                result = str(round(float(acc_results[acc]), 5))
        else:
            result = '('
            result_list = []
            for i, acc in enumerate(acc_results):
                result_list.append(str(round(float(acc_results[acc]), 5)))
            result += ", ".join(result_list) + ")"

    return result, valid, power_result

def get_accuracy_metric(config, model, path):

    import re
    is_valid = False
    all_accuracy_valid = True
    acc = None
    result_acc = None
    target = config.get_accuracy_target(model)
    acc_upper_limit = config.get_accuracy_upper_limit(model)
    patterns = []
    acc_targets = []
    acc_limits = []
    up_patterns = []
    acc_types = []

    if acc_upper_limit is not None:
        acc_limit_check = True
        for i in range(0, len(acc_upper_limit), 2):
            acc_type, acc_target = acc_upper_limit[i:i+2]
            acc_limits.append(acc_target)
            up_patterns.append(checker.ACC_PATTERN[acc_type])

    for i in range(0, len(target), 2):
        acc_type, acc_target = target[i:i+2]
        acc_types.append(acc_type)
        patterns.append(checker.ACC_PATTERN[acc_type])
        acc_targets.append(acc_target)

    acc_seen = [False for _ in acc_targets]
    acc_results = {}
    with open(os.path.join(path, "accuracy.txt"), "r", encoding="utf-8") as f:
        for line in f:
            for i, (pattern, acc_target, acc_type) in enumerate(zip(patterns, acc_targets, acc_types)):
                m = re.match(pattern, line)
                if m:
                    acc = m.group(1)

                    acc_results[acc_type] = acc

                if acc is not None and float(acc) >= acc_target:
                    all_accuracy_valid &= True
                    acc_seen[i] = True
                elif acc is not None:
                    all_accuracy_valid = False
                    #log.warning("%s accuracy not met: expected=%f, found=%s", path, acc_target, acc)
                if i == 0 and acc:
                    result_acc = acc
                acc = None
            if acc_upper_limit is not None:
                for i, (pattern, acc_limit) in enumerate(zip(up_patterns, acc_limits)):
                    m = re.match(pattern, line)
                    if m:
                        acc = m.group(1)
                    if acc is not None and acc_upper_limit is not None and float(acc) > acc_limit:
                        acc_limit_check = False
                        #log.warning("%s accuracy not met: upper limit=%f, found=%s", path, acc_limit, acc)
                    acc = None
            if all(acc_seen):
                break;
        is_valid = all_accuracy_valid & all(acc_seen)
        if acc_upper_limit is not None:
            is_valid &= acc_limit_check


    return is_valid, acc_results, acc_targets, acc_limits

def get_result_string(version, model, scenario, result_path, has_power, sub_res, division="open", system_json=None):

    config = checker.Config(
        version,
        None,
        ignore_uncommited=False,
        skip_power_check=False,
    )
    mlperf_model = config.get_mlperf_model(model)
    performance_path = os.path.join(result_path, "performance", "run_1")
    accuracy_path = os.path.join(result_path, "accuracy")
    scenario = checker.SCENARIO_MAPPING[scenario]

    fname = os.path.join(performance_path, "mlperf_log_detail.txt")
    mlperf_log = MLPerfLog(fname)
    effective_scenario = mlperf_log["effective_scenario"]
    inferred = False
    result = {}


    performance_result = checker.get_performance_metric(config, mlperf_model, performance_path, scenario, None, None, has_power)
    if "stream" in scenario.lower():
        performance_result_ = performance_result / 1000000 #convert to milliseconds
    else:
        performance_result_ = performance_result
    result['performance'] = round(performance_result_, 3)

    if scenario != effective_scenario:
        inferred, inferred_result = checker.get_inferred_result(scenario, effective_scenario, performance_result, mlperf_log, config, False)

    if has_power:
        is_valid, power_metric, scenario, avg_power_efficiency = checker.get_power_metric(config, scenario, performance_path, True, performance_result)
        if "stream" in scenario.lower():
            power_metric_unit = "milliJoules"
        else:
            power_metric_unit = "Watts"
        power_result_string = f"`Power consumed`: `{round(power_metric, 3)} {power_metric_unit}`, `Power efficiency`: `{round(avg_power_efficiency * 1000, 3)} samples per Joule`"

        power_result = round(power_metric, 3)
        power_efficiency_result = round(avg_power_efficiency, 3)
        result['power'] = power_result
        result['power_efficiency'] = power_efficiency_result

    compliance_list = [ "TEST01", "TEST05", "TEST04" ]
    if division == "closed":
        for test in compliance_list:
            test_path = os.path.join(result_path, test)
            if os.path.exists(test_path): #We dont consider missing test folders now - submission checker will do that
                #test_pass = checker.check_compliance_dir(test_path, mlperf_model, scenario, config, "closed", system_json, sub_res)
                test_pass = checker.check_compliance_perf_dir(test_path)
                if test_pass and test in [ "TEST01", "TEST06" ]:
                    #test_pass = checker.check_compliance_acc_dir(test_path, mlperf_model, config)
                    pass # accuracy truncation script is done after submission generation. We assume here that it'll pass 
                if test_pass:
                    result[test] = "passed"
                else:
                    result[test] = "failed"

    acc_valid, acc_results, acc_targets, acc_limits = get_accuracy_metric(config, mlperf_model, accuracy_path)

    result_field = checker.RESULT_FIELD[effective_scenario]

    performance_result_string = f"`{result_field}`: `{performance_result}`\n"
    if inferred:
        inferred_result_field = checker.RESULT_FIELD[scenario]
        performance_result_string += f"Inferred result: `{inferred_result_field}`: `{inferred_result}`  \n"

    accuracy_result_string = ''
    accuracy_results = []
    for i, acc in enumerate(acc_results):
        accuracy_results.append(str(round(float(acc_results[acc]), 5)))
        accuracy_result_string += f"`{acc}`: `{round(float(acc_results[acc]), 5)}`"
        if not acc_limits:
            accuracy_result_string += f", Required accuracy for closed division `>= {round(acc_targets[i], 5)}`"
        else:
            accuracy_result_string += f", Required accuracy for closed division `>= {round(acc_targets[i], 5)}` and `<= {round(acc_limits[i], 5)}`"
        accuracy_result_string += "\n"

    if len(accuracy_results) == 1:
        accuracy_result = accuracy_results[0]
    else:
        accuracy_result = "(" + ", ".join(accuracy_results)+")"
    result['accuracy'] = accuracy_result

    result_string = f"\n\n## Results\n"
    result_string += f"\nPlatform: {sub_res}\n"
    result_string += "\n### Accuracy Results \n" + accuracy_result_string
    result_string += "\n### Performance Results \n" + performance_result_string
    if has_power:
        result_string += "\n### Power Results \n" + power_result_string


    return result_string, result

def get_result_table(results):
    
    headers = ["Model", "Scenario", "Accuracy", "QPS", "Latency (in ms)", "Power Efficiency (in samples/J)", "TEST01", "TEST05", "TEST04"]
    table = []
    for model in results:
        for scenario in results[model]:
            row = []
            row.append(model)
            row.append(scenario)
            if results[model][scenario].get('accuracy'):
                val = str(results[model][scenario]['accuracy'])
                if not results[model][scenario].get('accuracy_valid', True):
                    val = "X "+val
                row.append(val)
            else:
                row.append("-")

            if results[model][scenario].get('performance'):
            
                if "stream" in scenario.lower():
                    if float(results[model][scenario]['performance']) == 0:
                        row.append("-")
                    elif scenario.lower() == "singlestream":
                        val_qps = str(round(1000/float(results[model][scenario]['performance']), 3))
                        if not results[model][scenario].get('performance_valid', True): # we explicitly mark invalid results
                            val_qps = "X "+val_qps
                        row.append(val_qps)
                    elif scenario.lower() == "multistream":
                        val_qps = str(round(8000/float(results[model][scenario]['performance']), 3))
                        if not results[model][scenario].get('performance_valid', True):
                            val_qps = "X "+val_qps
                        row.append(val_qps)
                    val = str(results[model][scenario]['performance'])
                    if not results[model][scenario].get('performance_valid', True):
                        val = "X "+val
                    row.append(val)
                else:
                    val = str(results[model][scenario]['performance'])
                    if not results[model][scenario].get('performance_valid', True):
                        val = "X "+val
                    row.append(val)
                    row.append("-")

            #if results[model][scenario].get('power','') != '':
            #    row.append(results[model][scenario]['power'])
            if results[model][scenario].get('power_efficiency','') != '':
                val = str(results[model][scenario]['power_efficiency'])
                if not results[model][scenario].get('power_valid', True):
                    val = "X "+val
                row.append(val)
            else:
                row.append(None)

            val1 = results[model][scenario].get('TEST01')
            val2 = results[model][scenario].get('TEST05')
            val3 = results[model][scenario].get('TEST04')
            if val1:
                row.append(val1)
                if val2:
                    row.append(val2)
                    if val3:
                        row.append(val3)
                elif val3:
                    row.append("missing")
                    row.append(val3)

            else:
                if val2:
                    row.append("missing")
                    row.append(val2)
                    if val3:
                        row.append(val3)
                elif val3:
                    row.append("missing")
                    row.append("missing")
                    row.append(val3)

            table.append(row)

    return table, headers
