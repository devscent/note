from fastapi import APIRouter, Query
import random
import string
import asyncio
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

def create_string_array(count):
    min_length = 30  # 최소 길이
    max_length = 45  # 최대 길이
    
    # 시드를 고정하여 호출마다 동일한 결과를 생성
    random.seed(42)
    
    result = []
    for _ in range(count):
        length = random.randint(min_length, max_length)
        random_string = ''.join(random.choices(string.ascii_letters, k=length))
        result.append(random_string)
    
    return result

@router.get("/tables")
async def get_tables(databaseType: str, sites: str):
    # if database_type == 'marsprimedb':
    #     raise HTTPException(status_code=400)

    await asyncio.sleep(1)
    # print(23)
    if databaseType == 'marsprimedb':
        splist = []
        splist.append('tbl_EQInfo')
        splist.append('tbl_EQInfo_FetchingHistory')
        splist.append('tbl_EQInfo_FTP')
        splist.append('tbl_EQCfgref3')
        splist.append('tbl_DailyStateSummary')
        splist.extend(create_string_array(20))

        return {
            "status": "success",
            "data": splist
        }
    elif databaseType == 'processdb':
        splist = []
        splist.append('tbl_EqPMStateHistory')
        splist.append('tbl_EqRobotMotionHistory')
        splist.append('tbl_EqHWMotionHistory')
        splist.extend(create_string_array(20))

        # 결과 반환
        return {
            "status": "success",
            "data": splist
        }
    elif databaseType == 'extsystemdb':
        splist = []
        splist.append('tbl_EQInfo_TPSS')
        splist.extend(create_string_array(20))

        # 결과 반환
        return {
            "status": "success",
            "data": splist
        }    

@router.get("/servers/{host_name}/databases/{database_name}/tables/{procedure_name}")
async def get_table_definition(host_name: str, database_name: str, procedure_name: str, datetime: Optional[str] = Query(None)):

    # await asyncio.sleep(1)  # 3초 동안 지연
    # print('timeout')

    # db = marsdb.DatabaseManager()
    # df = db.execute_stored_procedure(database='MARSPrimeDB', sp_name='Get_Lot_Transn_Fetch', sp_params={'LineCode':'AAAB'})

    with open("procedure1.txt", "r", encoding="utf-8") as file:
        content1 = file.read()
    with open("procedure2.txt", "r", encoding="utf-8") as file:
        content2 = file.read()
    with open("procedure3.txt", "r", encoding="utf-8") as file:
        content3 = file.read()

    if datetime:
        definitions = {
            'kimarsdb': procedure_name + "aaaaa" + datetime,
            'kmmarsdb': procedure_name + "aaaaa" + datetime,
            'kmmarsdb01': procedure_name + "aaaaa" + datetime,
            'kmmarsdb02': content1 + datetime,
            'kmmarsdb03': content2 + datetime,
            'kmmarsdb04': content3 + datetime,
            'kmmarsdb05': procedure_name + "aaaac" + datetime,
            'kmmarsdb06': "not exist" + datetime,
            'kmmarsdb07': "not exist" + datetime,
            'kmmarsdb08': "not exist" + datetime,
            'kmmarsdb09': "not exist" + datetime,
            'kmmarsdb10': "not exist" + datetime,
            'kmmarsdb11': "not exist" + datetime,
            'kmmarsdb12': "not exist" + datetime,
            'kmmarsdb13': "not exist" + datetime,
            'kmmarsdb14': "not exist" + datetime,
        }
    else:
        definitions = {
            'kimarsdb': procedure_name + "aaaaa",
            'kmmarsdb': procedure_name + "aaaaa",
            'kmmarsdb01': procedure_name + "aaaaa",
            'kmmarsdb02': content1,
            'kmmarsdb03': content2,
            'kmmarsdb04': content3,
            'kmmarsdb05': procedure_name + "aaaac",
            'kmmarsdb06': "not exist",
            'kmmarsdb07': "not exist",
            'kmmarsdb08': "not exist",
            'kmmarsdb09': "not exist",
            'kmmarsdb10': "not exist",
            'kmmarsdb11': "not exist",
            'kmmarsdb12': "not exist",
            'kmmarsdb13': "not exist",
            'kmmarsdb14': "not exist",
        }
    
    return {
            "status": "success",
            "data": {
                "host_name": host_name,
                "database_name": database_name,
                "procedure_name": procedure_name,
                "definition": definitions[host_name]
            }
        }
        
