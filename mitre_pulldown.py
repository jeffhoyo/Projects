# Author: eTAFTo
# Date: August 14, 2019
# Title: Extraction of MITRE ATT&CK Matrix (TTPs to Groups)
# pip install attackcti

from attackcti import attack_client
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np

lift = attack_client()
enterprise_groups = lift.get_enterprise_groups(stix_format=False)

# Created empty dataframe
t2g_df = pd.DataFrame()

# iterate thru all enterprise groups
for i in range(0, len(enterprise_groups)):

    # extract actual group name
    group_name = enterprise_groups[i]['group']

    # These two groups have bad data. They identify to have used all techniques.
    if group_name in ['APT34', 'MONSOON']:
        pass
    else:

        # given the group number, identify all techniques
        techniques_by_group = lift.get_techniques_used_by_group(enterprise_groups[i], stix_format=False)

        # Created a filter for groups that do not contain any techniques
        if len(techniques_by_group) == 0:
            print('Progress : ' + str(i) + ' of ' + str(len(enterprise_groups)))
            pass
        else:

            # normalized or converted the JSON file into a dataframe
            t2g_normalized = json_normalize(techniques_by_group)

            # created a filter for platform (a.k.a OS)
            if "platform" in t2g_normalized.columns:

                # filter for platforms with Windows Only
                platform_list = []
                t2g_normalized['platform'] = t2g_normalized['platform'].replace(np.nan, 0)
                for sublst in t2g_normalized['platform']:
                    if sublst == 0:
                        platform_list.append(0)
                    else:
                        platform_list.append(", ".join(sublst))
                t2g_normalized['platform'] = platform_list
                t2g_normalized = t2g_normalized[t2g_normalized['platform'].str.contains("Windows").notnull()]

                # Create the data frame (add new column with null values; created the dataframe, added binary values to the group, and dropped null values)
                t2g_normalized[group_name] = np.nan
                t2g_normalized = pd.DataFrame(t2g_normalized[['tactic', 'technique', 'technique_id', group_name]])
                t2g_normalized[group_name] = 1
                t2g_normalized = t2g_normalized.dropna()

                # extracted the list values, converted to strings, then created a column with string values
                tactic_list = []
                for sublst in t2g_normalized['tactic']:
                    tactic_list.append(", ".join(sublst))
                t2g_normalized['tactic'] = tactic_list

                # Merge tables
                if i == 0:
                    # populated the main table
                    t2g_df = t2g_normalized
                else:
                    # Merged tables on three columns
                    t2g_df = t2g_df.merge(t2g_normalized, how='outer', on=['tactic', 'technique', 'technique_id'])
                print('Progress : ' + str(i) + ' of ' + str(len(enterprise_groups)))
            else:
                print('Progress : ' + str(i) + ' of ' + str(len(enterprise_groups)))

# Renamed the Index
t2g_df = t2g_df.shift()[1:]

# Print the shape
t2g_df.shape

# Create CSV
t2g_df.to_csv("group_output")
