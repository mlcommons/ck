This README provides a walkthrough of the `_cm.yaml` file.

## Keys and Datatypes followed

1. **alias**: `string`
2. **uid**: `string`
3. **automation_alias**: `string`
4. **automation_uid**: `string`
5. **category**: `string`
6. **developers**: `list of strings`
7. **tags**: `list of strings`
8. **default_env**: `dictionary` - Contains key-value pairs where values are `strings`
9. **env**: `dictionary` - Contains key-value pairs where values are `strings`
10. **input_mapping**: `dictionary` - Contains key-value pairs where values are `strings`
11. **env_key_mapping**: `dictionary` - Contains key-value pairs where values are `strings`
12. **new_env_keys**: `list of strings`
13. **new_state_keys**: `list of strings`
14. **deps**: `list of dictionaries` - Each dictionary can contain `tags` or other nested keys
15. **names**: `list of strings`
16. **enable_if_env**: `dictionary` - Contains key-value pairs where values are lists of `strings`
17. **skip_if_env**: `dictionary` - Contains key-value pairs where values are lists of `strings`
18. **prehook_deps**: `list of dictionaries` - Each dictionary may contain `names` and `tags` as lists
19. **posthook_deps**: `list of dictionaries` - Each dictionary may contain `tags` and other keys
20. **variation_groups_order**: `list of strings`
21. **variations**: `dictionary` - Each variation is a dictionary containing keys like `alias`, `default_variations`, `group`, etc.
22. **group**: `string`
23. **add_deps_recursive**: `dictionary` - Contains nested `tags` and other keys
24. **default_variations**: `dictionary` - Contains key-value pairs where values are `strings`
25. **docker**: `dictionary` - Contains keys specific to Docker configurations:
    - **base_image**: `string`
    - **image_name**: `string`
    - **os**: `string`
    - **os_version**: `string`
    - **deps**: `list of dictionaries` - Each dictionary can include `tags` or other keys.
    - **env**: `dictionary` - Contains key-value pairs where values are `strings`
    - **interactive**: `boolean`
    - **extra_run_args**: `string`
    - **mounts**: `list of strings` - Specifies mount paths in the format `"source:destination"`
    - **pre_run_cmds**: `list of strings` - Commands to run before the container starts
    - **docker_input_mapping**: `dictionary` - Contains key-value pairs where values are strings, mapping input parameters to Docker environment variables
    - **use_host_user_id**: `boolean`
    - **use_host_group_id**: `boolean`
    - **skip_run_cmd**: `string`
    - **shm_size**: `string`
    - **real_run**: `boolean`
    - **all_gpus**: `string`
