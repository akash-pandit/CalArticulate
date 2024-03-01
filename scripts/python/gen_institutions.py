import requests
import json

def gen_institutions_dict() -> dict[str, str]:
    institutions = dict()

    try:
        response = requests.get("https://assist.org/api/institutions", timeout=5)
        response.raise_for_status()
        institution_list = response.json()

        # populate institutions.json
        for raw_inst_dict in institution_list:
            inst_id = raw_inst_dict['id']
            inst_primary_name = raw_inst_dict['names'][0]['name']

            institutions[inst_id] = inst_primary_name

        # first name is 'California Maritime Academy' in api, assist redirects to the latter
        institutions[1] = 'California State University, Maritime Academy'

    # catch any possible exception and log to stdout
    except requests.Timeout:
        print("The request timed out.")
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.ConnectionError:
        print("Failed to establish a connection.")
    except ValueError as val_err:
        print("Invalid JSON received:", val_err)
    except requests.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    return institutions

    
    
def main() -> None:
    inst_dict = gen_institutions_dict()

    if not inst_dict:
        raise Exception("An unexpected error occured that evaded all try except clauses")
    
    cc_insts = dict()
    state_insts = dict()
    
    for id, name in inst_dict.items():
        if 'University' in name:
            state_insts[id] = name
        else:
            cc_insts[id] = name

    with open('./data/institutions_state.json', 'w') as file:
        json.dump(state_insts, file, indent=4)

    print("State institutions (CSUs/UCs) stored")
    
    with open('./data/institutions_cc.json', 'w') as file:
        json.dump(cc_insts, file, indent=4)

    print("California CC institutions stored")


if __name__ == '__main__':
    main()