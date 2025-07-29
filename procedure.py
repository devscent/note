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

@router.get("/servers/databases")
async def get_server_db_mapping():
    server_db_data ={
        "regions": {
            "domestic": {
                "MEM": {
                    "kmmarsdb": ["cleanmemdb", "cmpmemdb"],
                    "kmmarsdb01": ["diffmemdb", "metalmemdb"],
                    "kmmarsdb02": ["impmemdb", "metromemdb", "photomemdb", "photospinnerdb"],
                    "kmmarsdb03": ["etchmemdb"],
                    "kmmarsdb04": ["cvdmemdb"]
                },
                "FDY": {
                    "kimarsdb": ["cleanmemdb", "cmpmemdb", "diffmemdb", "metalmemdb", "impmemdb", "etchmemdb"]
                }
            },
            "overseas": {
                "SC": {
                    "x2marsdb1": ["cleanmemdb", "cmpmemdb", "diffmemdb", "metalmemdb", "impmemdb", "etchmemdb"]
                },
                "SA": {
                    "s2cluseter": ["cleanmemdb", "cmpmemdb", "diffmemdb", "metalmemdb", "impmemdb", "etchmemdb"]
                }
            }
        }
    }

    return {
        "status": "success",
        "data": server_db_data
    }

@router.get("/procedures")
async def get_procedures(databaseType: str, sites: str):
    # if database_type == 'marsprimedb':
    #     raise HTTPException(status_code=400)

    await asyncio.sleep(1)
    # print(23)
    if databaseType == 'marsprimedb':
        splist = []
        splist.append('GetEQJobInfo')
        splist.append('Insert_SEOS')
        splist.append('Insert_STDailySummary_Chambers')
        splist.append('Insert_STDailySummary_Chambers_Month')
        splist.append('Insert_STDailySummary_Chambers_Week')
        splist.append('Update_EQInfo')
        splist.append('Update_EQInfo_History')
        splist.append('Update_EQInfo_Offline')
        splist.extend(create_string_array(20))

        return {
            "status": "success",
            "data": splist
        }
    elif databaseType == 'processdb':
        splist = []
        splist.append('Delete_JobData')
        splist.append('Exec_DailyProessingSPs_ByEQ')
        splist.append('Exec_QrtlNonProcess_ByEQ')
        splist.append('Exec_QuartileSPs_ByEQ')
        splist.append('GetLotHistory')
        splist.append('GetParsingRule')
        splist.append('Insert_StateInfo_PM')
        splist.append('Insert_StateInfo_HWTime')
        splist.append('Insert_StateInfo_RobotMotion')
        splist.extend(create_string_array(20))

        # 결과 반환
        return {
            "status": "success",
            "data": splist
        }
    elif databaseType == 'extsystemdb':
        splist = []
        splist.append('GetIF_MI_EQP_HIST')
        splist.append('Insert_EQInfo_TPSS')
        splist.append('Insert_IPAddress_TC')
        splist.append('Insert_IPAddress_TC200')
        splist.append('Truncate_TPSS_Port_History')
        splist.extend(create_string_array(20))

        # 결과 반환
        return {
            "status": "success",
            "data": splist
        }    
    
@router.get("/servers/{host_name}/databases/{database_name}/procedures/{procedure_name}")
async def get_procedure_definition(host_name: str, database_name: str, procedure_name: str, datetime: Optional[str] = Query(None)):

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
            'kmmarsdb01': "not exist",
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
    
@router.get("/servers/{host_name}/databases/{database_name}/procedures/{procedure_name}/histories")
async def get_procedure_definition_histories(host_name: str, database_name: str, procedure_name: str, fields: str):

    # db = marsdb.DatabaseManager()
    # df = db.execute_stored_procedure(database='MARSPrimeDB', sp_name='Get_Lot_Transn_Fetch', sp_params={'LineCode':'AAAB'})

    if host_name == 'kmmarsdb':
        return {
            "status": "success",
            "history": ['2024-08-16 18:48:02.110',
                        '2024-08-17 22:13:31.989',
                        '2024-08-19 01:39:01.868',
                        '2024-08-20 05:04:31.747',
                        '2024-08-21 08:30:01.626',
                        '2024-08-22 11:55:31.505',
                        '2024-08-23 15:21:01.384',
                        '2024-08-24 18:46:31.263',
                        '2024-08-25 22:12:01.142',
                        '2024-08-27 01:37:31.021',
                        '2024-08-28 05:03:00.901',
                        '2024-08-28 05:03:00.902',
                        '2024-08-28 05:03:00.903',
                        '2024-08-28 05:03:00.904',
                        '2024-08-28 05:03:00.905',
                        '2024-08-28 05:03:00.906',
                        '2024-08-28 05:03:00.907',
                        '2024-08-28 05:03:00.908',
                        '2024-08-28 05:03:00.909',
                        '2024-08-28 05:03:00.910',
                        '2024-08-28 05:03:00.911',
                        '2024-08-29 08:28:30.779']
        }
    elif host_name == 'kmmarsdb01':
        return {
            "status": "success",
            "history": ['2024-08-21 08:30:01.626',"2024-09-13 13:22:32.231","2024-09-14 11:22:32.231","2024-09-15 15:22:32.231"]
        }
    elif host_name == 'kmmarsdb02':
        return {
            "status": "success",
            "history": ['2024-08-21 08:30:01.626',"2024-08-13 13:22:32.231","2024-08-14 11:22:32.231","2024-08-15 15:22:32.231"]
        }
    elif host_name == 'kmmarsdb03':
        return {
            "status": "success",
            "history": ["2024-08-13 13:22:32.231","2024-08-14 11:22:32.231","2024-08-15 15:22:32.231"]
        }
    elif host_name == 'kmmarsdb04':
        return {
            "status": "success",
            "history": ["2024-08-13 13:22:32.231","2024-08-14 11:22:32.231","2024-08-15 15:22:32.231"]
        }
    elif host_name == 'kmmarsdb05':
        return {
            "status": "success",
            "history": ["2024-08-13 13:22:32","2024-08-14 11:22:32","2024-08-15 15:22:32"]
        }
    elif host_name == 'kmmarsdb06':
        # await asyncio.sleep(5)
        # raise HTTPException(status_code=400)
        return {
            "status": "fail",
            "data": {
                "host_name": host_name,
                "database_name": database_name,
                "procedure_name" : procedure_name,
                "definition" : procedure_name + "aaaae",
            }
        }
    elif host_name == 'kmmarsdb07':
        return {
            "status": "success",
            "data": {
                "host_name": host_name,
                "database_name": database_name,
                "procedure_name" : procedure_name,
                "definition" : "not exist"
            }
        }    

class StoredProcedureUpdate(BaseModel):
    definition :str

@router.put("/servers/{host_name}/databases/{database_name}/procedures/{procedure_name}")
async def update_procedure(host_name: str, database_name: str, procedure_name: str, sp_update: StoredProcedureUpdate):
    """
    특정 서버의 특정 데이터베이스에 있는 프로시저 업데이트 API
    """

    return {"status": "success", "message": f"Stored procedure '{procedure_name}' in database '{database_name}' updated successfully."}
