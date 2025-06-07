import os
import subprocess

root_dir = os.environ.get("GITHUB_WORKSPACE", ".")
print(f"Deploying all Snowpark apps in root directory {root_dir}")

for dirpath, dirnames, filenames in os.walk(root_dir):
    if 'snowflake.yml' in filenames:
        print(f"Found Snowflake project in folder {dirpath}")
        os.chdir(dirpath)
        subprocess.run(
            [
                "snow", "app", "run",
                "--connection", "user_connection"
            ],
            check=True,
            env={
                **os.environ,
                "SNOWFLAKE_ACCOUNT": os.environ.get("SNOWFLAKE_ACCOUNT", "QA88598"),
                "SNOWFLAKE_USER": os.environ.get("SNOWFLAKE_USER", "sandeep2910"),
                "SNOWFLAKE_PASSWORD": os.environ.get("SNOWFLAKE_PASSWORD", "Harihara@292707"),
                "SNOWFLAKE_ROLE": os.environ.get("SNOWFLAKE_ROLE", "ACCOUNTADMIN"),
                "SNOWFLAKE_WAREHOUSE": os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
                "SNOWFLAKE_DATABASE": os.environ.get("SNOWFLAKE_DATABASE", "snowpark_app"),
                "SNOWFLAKE_SCHEMA": os.environ.get("SNOWFLAKE_SCHEMA", "snowparkapp_schema"),
            }
        )





# import os
# import subprocess

# root_dir = os.environ.get("GITHUB_WORKSPACE", ".")
# print(f"Deploying all Snowpark apps in root directory {root_dir}")

# for dirpath, dirnames, filenames in os.walk(root_dir):
#     if 'snowflake.yml' in filenames:
#         print(f"Found Snowflake project in folder {dirpath}")
#         os.chdir(dirpath)
#         subprocess.run(["snow", "app", "run"], check=True)




# import sys
# import os
# import yaml

# ignore_folders = ['.git', '__pycache__', '.ipynb_checkpoints']
# snowflake_project_config_filename = 'snowflake.yml'

# if len(sys.argv) != 2:
#     print("Root directory is required")
#     exit()

# root_directory = sys.argv[1]
# print(f"Deploying all Snowpark apps in root directory {root_directory}")

# for (directory_path, directory_names, file_names) in os.walk(root_directory):
#     base_name = os.path.basename(directory_path)
#     if base_name in ignore_folders:
#         continue
#     if snowflake_project_config_filename not in file_names:
#         continue

#     print(f"Found Snowflake project in folder {directory_path}")

#     with open(f"{directory_path}/{snowflake_project_config_filename}", "r") as yamlfile:
#         project_settings = yaml.load(yamlfile, Loader=yaml.FullLoader)

#     # if 'snowpark' not in project_settings:
#     #     print(f"Skipping non Snowpark project in folder {base_name}")
#     #     continue

#     # Confirm that this is a Snowpark project (Definition v2 check)
#     if 'execution' not in project_settings:
#         print(f"Skipping non Snowpark project in folder {base_name}")
#         continue

#     # Use fallback if 'name' is not in v2 schema
#     project_name = project_settings.get('name', base_name)
#     print(f"Found Snowflake Snowpark project '{project_name}' in folder {base_name}")

#     # project_name = project_settings['snowpark'].get('project_name', 'UNKNOWN_PROJECT')
#     # print(f"Found Snowflake Snowpark project '{project_name}' in folder {base_name}")
#     print(f"Calling snowcli to deploy the project")
#     os.chdir(f"{directory_path}")
#     os.system(f"snow snowpark build --temporary-connection --account $SNOWFLAKE_ACCOUNT --user $SNOWFLAKE_USER --role $SNOWFLAKE_ROLE --warehouse $SNOWFLAKE_WAREHOUSE --database $SNOWFLAKE_DATABASE")
#     os.system(f"snow snowpark deploy --replace --temporary-connection --account $SNOWFLAKE_ACCOUNT --user $SNOWFLAKE_USER --role $SNOWFLAKE_ROLE --warehouse $SNOWFLAKE_WAREHOUSE --database $SNOWFLAKE_DATABASE")











# import sys
# import os
# import yaml

# ignore_folders = ['.git', '__pycache__', '.ipynb_checkpoints']
# snowflake_project_config_filename = 'snowflake.yml'

# if len(sys.argv) != 2:
#     print("Root directory is required")
#     exit()

# root_directory = sys.argv[1]
# print(f"Deploying all Snowpark apps in root directory {root_directory}")

# # Walk the entire directory structure recursively
# for (directory_path, directory_names, file_names) in os.walk(root_directory):
#     # Get just the last/final folder name in the directory path
#     base_name = os.path.basename(directory_path)

#     # Skip any folders we want to ignore
#     # TODO: Update this logic to skip all subfolders of ignored folder
#     if base_name in ignore_folders:
# #        print(f"Skipping ignored folder {directory_path}")
#         continue

#     # An snowflake.yml file in the folder is our indication that this folder contains
#     # a Snow CLI project
#     if not snowflake_project_config_filename in file_names:
# #        print(f"Skipping non-app folder {directory_path}")
#         continue
#     print(f"Found Snowflake project in folder {directory_path}")

#     # Read the project config
#     project_settings = {}
#     with open(f"{directory_path}/{snowflake_project_config_filename}", "r") as yamlfile:
#         project_settings = yaml.load(yamlfile, Loader=yaml.FullLoader)

#     # Confirm that this is a Snowpark project
#     # TODO: Would be better if the project config file had a project_type key!
#     if 'snowpark' not in project_settings:
#         print(f"Skipping non Snowpark project in folder {base_name}")
#         continue

#     # Finally deploy the Snowpark project with the snowcli tool
#     #print(f"Found Snowflake Snowpark project '{project_settings['snowpark']['project_name']}' in folder {base_name}")
#     project_name = project_settings.get('project_name', 'UNKNOWN_PROJECT')
#     print(f"Found Snowflake Snowpark project '{project_name}' in folder {base_name}")
#     print(f"Calling snowcli to deploy the project")
#     os.chdir(f"{directory_path}")
#     # Make sure all 6 SNOWFLAKE_ environment variables are set
#     # SnowCLI accesses the passowrd directly from the SNOWFLAKE_PASSWORD environmnet variable
#     os.system(f"snow snowpark build --temporary-connection --account $SNOWFLAKE_ACCOUNT --user $SNOWFLAKE_USER --role $SNOWFLAKE_ROLE --warehouse $SNOWFLAKE_WAREHOUSE --database $SNOWFLAKE_DATABASE")
#     os.system(f"snow snowpark deploy --replace --temporary-connection --account $SNOWFLAKE_ACCOUNT --user $SNOWFLAKE_USER --role $SNOWFLAKE_ROLE --warehouse $SNOWFLAKE_WAREHOUSE --database $SNOWFLAKE_DATABASE")