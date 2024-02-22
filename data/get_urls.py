import json
import requests


def get_ids(school_type: str) -> list[str]:
    """ returns dict_keys list of school ids. Valid inputs are 'cc' or 'state'. """
    with open(f'./data/institutions_{school_type}.json', 'r') as file:
        return json.load(file).keys()


def get_agreement_years(inst_id: str) -> dict[int, int]:
    """returns a dict with the agreement years between a given cc id and all state school ids"""
    # inst_id == cc_id, agreement_id == state_id
    response = requests.get(f"https://assist.org/api/institutions/{inst_id}/agreements")

    print(f"Reached URL for CC: {inst_id}")

    response.raise_for_status()
    institution_list = response.json()  # actually returns list of json objects
    
    agreement_years = dict()

    for inst_dict in institution_list:
        agreement_id = inst_dict['institutionParentId']  # state school id
        year = max(inst_dict['receivingYearIds'])  # most recent agreement year
        if year == 74:
            agreement_years[agreement_id] = year # don't need to care about outdated articulation agreements

    return agreement_years


def get_urls() -> dict[str, list]:
    # for future reference:
    # institution id: the 'home school' id which has agreements with state schools (cc)
    # agreement id: the id of the state school the institution has an agreement with

    inst_ids_state = get_ids("state")
    inst_ids_cc = get_ids("cc")

    agreement_yrs_dict = {cc_id : get_agreement_years(cc_id) for cc_id in inst_ids_cc}

    # agreement_years = {cc_id : 74 for cc_id in inst_ids_cc}  # use for testing to speed up runtime
    urls = {state_id : [] for state_id in inst_ids_state}

    for state_id in inst_ids_state:
        for cc_id in inst_ids_cc:
            
            year = agreement_yrs_dict[cc_id].get(int(state_id))
            if not year:
                continue  # there has never been an agreement between these institutions

            url = f"https://assist.org/transfer/results?year={year}&institution={cc_id}" + \
            f"&agreement={state_id}&agreementType=to&view=agreement&viewBy=major&viewSendingAgreements=false"

            urls[state_id].append(url)

    return urls


def output_urls() -> None:
    with open('./data/assist_urls.json', 'w') as file:
        json.dump(get_urls(), file, indent=4)


if __name__ == '__main__':
    output_urls()