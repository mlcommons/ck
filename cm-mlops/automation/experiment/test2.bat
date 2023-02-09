cm run experiment --tags=xyz @test_input.yaml -- echo %%VAR1%% {{VAR1}} {{VAR2}} {{VAR4{['xx','yy','zz']}}}-%%VAR3%% {{CM_EXPERIMENT_PATH3}}
