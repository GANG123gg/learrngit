import requests
import unittest
import xlrd
from ddt import ddt,data,unpack
from HTMLTestRunner import HTMLTestRunner
from Zong_TingChe.port.zong_PortRequest import Request_Method_Package
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from Zong_TingChe.MysqlConnect.mysql_connect import mysql_connect_zong


def get_zong_xls(filexpath,sheet,start,end):
        '''
        封装批量读取Excel数据
        :param filexpath:
        :return:
        '''
        list_values = []
        file = xlrd.open_workbook(filexpath)
        table = file.sheet_by_name(sheet)
        #rows = table.nrows
        for i in range(start,end):
            list_values.append(table.row_values(i))
        return list_values

#单次计费
duration_list_values = (r'zong_dura_charge_test.xls')
duration_list_user = 'DurationUser'
duration_list_charge = 'DurationCharge'
duration_list_charge_update = 'DurationChargeUpdate'
duration_list_service_add = 'DurationServiceAdd'
duration_list_datas = 'DurationDate'
duration_list_service_del = 'DurationServiceDel'
duration_list_charge_del = 'DurationChargeDel'

@ddt
class Charg_Zong(unittest.TestCase,OperaPage_Login,mysql_connect_zong):

    @classmethod
    def setUpClass(self) -> None:
        self.request = Request_Method_Package()

    user_login = get_zong_xls(duration_list_values,duration_list_user,1,2)
    user_login_data = list(user_login)
    @data(*user_login_data)
    @unpack
    def test01_login(self,head,postdata,url):#登录
        self.log_port_zong(head)
        datatest = eval(postdata)
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path ,json=datatest,token_get='result')
        print(self.res)
        self.assertEqual(self.res['code'],200)

    '''
    创建按时长计算的计费规则
    '''
    dura_charge_add = get_zong_xls(duration_list_values,duration_list_charge,1,2)
    dura_charge_add_data = list(dura_charge_add)
    @data(*dura_charge_add_data)
    @unpack
    def test02_charge_add(self,head,parkid,parkname,vehicleTypeId,url):#创建计费规则
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "parkId":int(parkid),
                        "parkName":parkname,
                        "regions":[

                        ],
                        "freeTimes":"0",
                        "vehicleTypeId":int(vehicleTypeId),
                        "state":1,
                        "chargeTimes":[

                        ],
                        "serviceTypeCode":-1,
                        "payoutValidity":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "intervalMaxCharge":"0",
                                "scaleFee":"0.03",
                                "scaleTimes":"60",
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":"60",
                                        "scaleTimes":"60",
                                        "scaleFee":"0.03"
                                    },
                                    {
                                        "chargeStart":"60",
                                        "scaleFee":"0.02",
                                        "scaleTimes":"60"
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    # dura_service_add = get_zong_xls(duration_list_values,duration_list_service_add,1,7)
    # dura_service_add_data = list(dura_service_add)
    # @data(*dura_service_add_data)
    # @unpack
    # def test03(self,head,postdata,url):#新增服务车辆
    #     self.log_port_zong(head)
    #     datatest = eval(postdata)
    #     url_path = url
    #     self.res = self.request.SendRequest(method='post',url=url_path,json=datatest)
    #     self.assertEqual(self.res['code'],200)

    dura_data_one = get_zong_xls(duration_list_values,duration_list_datas,1,2)
    dura_data_data_one = list(dura_data_one)
    @data(*dura_data_data_one)
    @unpack
    def test04(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":int(curChannelId),
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":int(regionId),
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":int(vehicleType),
                    "agentId":int(agentId),
                    "parkId":int(parkId)
                }
        print(datatest)
        url_path = url
        print(url_path)
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res['fee'])
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)


    '''
    增加免费时长
    '''
    dura_charge_upone = get_zong_xls(duration_list_values,duration_list_charge_update,1,2)
    dura_charge_upone_data = list(dura_charge_upone)
    @data(*dura_charge_upone_data)
    @unpack
    def test05_charge_update(self,head,parkid,parkname,vehicleTypeId,user,grammar,grammars,url):#修改计费规则—增加免费时长
        self.log_port_zong(head)
        idv = self.mysql_zong(grammar=grammar)
        ID = idv[0][0]
        rid = self.mysql_zong(grammar=grammars)
        RID = rid[0][0]
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "vehicleTypeId":int(vehicleTypeId),
                        "regions":[

                        ],
                        "parkName":parkname,
                        "ruleIntervalVo":{
                            "ruleDurations":[

                            ],
                            "chargeType":1,
                            "chargeWay":3,
                            "ruleIntervals":[
                                {
                                    "intervalMaxCharge":0,
                                    "dayPartingId":ID,
                                    "ruleDurations":[
                                        {
                                            "chargeStart":0,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "chargeEnd":60,
                                            "id":3263,
                                            "isRecharge":False,
                                            "scaleFee":0.03,
                                            "scaleTimes":60
                                        },
                                        {
                                            "chargeStart":60,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "id":3264,
                                            "isRecharge":False,
                                            "scaleFee":0.02,
                                            "scaleTimes":60
                                        }
                                    ],
                                    "startTime":"00:00:00",
                                    "endTime":"23:59:59",
                                    "id":RID,
                                    "scaleFee":0.03,
                                    "scaleTimes":60
                                }
                            ]
                        },
                        "parkId":int(parkid),
                        "freeTimes":"30",
                        "createBy":user,
                        "createTime":"2021-07-22 15:40:07",
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "id":ID,
                        "state":1,
                        "vehicleTypeName":"小车",
                        "serviceTypeCode":-1,
                        "maxCharge":-1,
                        "dayMaxCharge":-1,
                        "payoutValidity":-1,
                        "dayMaxChargeTotal":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "intervalMaxCharge":0,
                                "dayPartingId":ID,
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "id":RID,
                                "scaleFee":0.03,
                                "scaleTimes":60,
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":60,
                                        "scaleTimes":60,
                                        "scaleFee":0.03
                                    },
                                    {
                                        "chargeStart":60,
                                        "ruleIntervalId":RID,
                                        "dayPartingId":ID,
                                        "id":3264,
                                        "isRecharge":False,
                                        "scaleFee":0.02,
                                        "scaleTimes":60
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    dura_data_two = get_zong_xls(duration_list_values,duration_list_datas,3,6)
    dura_data_data_two = list(dura_data_two)
    @data(*dura_data_data_two)
    @unpack
    def test06(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":int(curChannelId),
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":int(regionId),
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":int(vehicleType),
                    "agentId":int(agentId),
                    "parkId":int(parkId)
                }
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)


    '''
    增加时段最高
    '''
    @data(*dura_charge_upone_data)
    @unpack
    def test07_charge_update(self,head,parkid,parkname,vehicleTypeId,user,grammar,grammars,url):#修改计费规则—增加时段最高
        self.log_port_zong(head)
        idv = self.mysql_zong(grammar=grammar)
        ID = idv[0][0]
        rid = self.mysql_zong(grammar=grammars)
        RID = rid[0][0]
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "vehicleTypeId":int(vehicleTypeId),
                        "regions":[

                        ],
                        "parkName":parkname,
                        "ruleIntervalVo":{
                            "dayMaxChargeTotal":"-1.00",
                            "maxCharge":"-1.00",
                            "ruleDurations":[

                            ],
                            "chargeType":1,
                            "chargeWay":2,
                            "dayMaxCharge":"-1.00",
                            "ruleIntervals":[
                                {
                                    "intervalMaxCharge":0,
                                    "dayPartingId":ID,
                                    "ruleDurations":[
                                        {
                                            "chargeStart":0,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "chargeEnd":60,
                                            "id":3277,
                                            "isRecharge":False,
                                            "scaleFee":0.03,
                                            "scaleTimes":60
                                        },
                                        {
                                            "chargeStart":60,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "id":3278,
                                            "isRecharge":False,
                                            "scaleFee":0.02,
                                            "scaleTimes":60
                                        }
                                    ],
                                    "startTime":"00:00:00",
                                    "endTime":"23:59:59",
                                    "id":RID,
                                    "scaleFee":0.03,
                                    "scaleTimes":60
                                }
                            ]
                        },
                        "parkId":int(parkid),
                        "freeTimes":30,
                        "createBy":user,
                        "createTime":"2021-07-22 17:23:03",
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "id":ID,
                        "state":1,
                        "vehicleTypeName":"小车",
                        "serviceTypeCode":-1,
                        "maxCharge":-1,
                        "dayMaxCharge":-1,
                        "dayMaxChargeTotal":-1,
                        "payoutValidity":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "intervalMaxCharge":"0.12",
                                "dayPartingId":ID,
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "id":RID,
                                "scaleFee":0.03,
                                "scaleTimes":60,
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":60,
                                        "scaleTimes":60,
                                        "scaleFee":0.03
                                    },
                                    {
                                        "chargeStart":60,
                                        "ruleIntervalId":RID,
                                        "dayPartingId":ID,
                                        "id":3278,
                                        "isRecharge":False,
                                        "scaleFee":0.02,
                                        "scaleTimes":60
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    dura_data_two = get_zong_xls(duration_list_values,duration_list_datas,7,10)
    dura_data_data_two = list(dura_data_two)
    @data(*dura_data_data_two)
    @unpack
    def test08(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":int(curChannelId),
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":int(regionId),
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":int(vehicleType),
                    "agentId":int(agentId),
                    "parkId":int(parkId)
                }
        self.log_port_zong(datatest)
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)


    '''
    设置首段费用大于时段最高
    '''
    @data(*dura_charge_upone_data)
    @unpack
    def test09_charge_update(self,head,parkid,parkname,vehicleTypeId,user,grammar,grammars,url):#修改计费规则—增加时段最高
        self.log_port_zong(head)
        idv = self.mysql_zong(grammar=grammar)
        ID = idv[0][0]
        rid = self.mysql_zong(grammar=grammars)
        RID = rid[0][0]
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "vehicleTypeId":int(vehicleTypeId),
                        "regions":[

                        ],
                        "parkName":parkname,
                        "ruleIntervalVo":{
                            "dayMaxChargeTotal":"-1.00",
                            "maxCharge":"-1.00",
                            "ruleDurations":[

                            ],
                            "chargeType":1,
                            "chargeWay":2,
                            "dayMaxCharge":"-1.00",
                            "ruleIntervals":[
                                {
                                    "intervalMaxCharge":0.12,
                                    "dayPartingId":ID,
                                    "ruleDurations":[
                                        {
                                            "chargeStart":0,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "chargeEnd":60,
                                            "id":3279,
                                            "isRecharge":False,
                                            "scaleFee":0.03,
                                            "scaleTimes":60
                                        },
                                        {
                                            "chargeStart":60,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "id":3280,
                                            "isRecharge":False,
                                            "scaleFee":0.02,
                                            "scaleTimes":60
                                        }
                                    ],
                                    "startTime":"00:00:00",
                                    "endTime":"23:59:59",
                                    "id":RID,
                                    "scaleFee":0.03,
                                    "scaleTimes":60
                                }
                            ]
                        },
                        "parkId":int(parkid),
                        "freeTimes":30,
                        "createBy":user,
                        "createTime":"2021-07-22 17:23:03",
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "id":ID,
                        "state":1,
                        "vehicleTypeName":"小车",
                        "serviceTypeCode":-1,
                        "maxCharge":-1,
                        "dayMaxCharge":-1,
                        "dayMaxChargeTotal":-1,
                        "payoutValidity":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "intervalMaxCharge":"0.02",
                                "dayPartingId":ID,
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "id":RID,
                                "scaleFee":0.03,
                                "scaleTimes":60,
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":60,
                                        "scaleTimes":60,
                                        "scaleFee":0.03
                                    },
                                    {
                                        "chargeStart":60,
                                        "ruleIntervalId":RID,
                                        "dayPartingId":ID,
                                        "id":3280,
                                        "isRecharge":False,
                                        "scaleFee":0.02,
                                        "scaleTimes":60
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    dura_data_two = get_zong_xls(duration_list_values,duration_list_datas,11,13)
    dura_data_data_two = list(dura_data_two)
    @data(*dura_data_data_two)
    @unpack
    def test10(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":curChannelId,
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":regionId,
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":vehicleType,
                    "agentId":agentId,
                    "parkId":parkId
                }
        self.log_port_zong(datatest)
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)


    '''
    增加单次限制
    '''
    @data(*dura_charge_upone_data)
    @unpack
    def test11_charge_update(self,head,parkid,parkname,vehicleTypeId,user,grammar,grammars,url):#修改计费规则—增加时段最高
        self.log_port_zong(head)
        idv = self.mysql_zong(grammar=grammar)
        ID = idv[0][0]
        rid = self.mysql_zong(grammar=grammars)
        RID = rid[0][0]
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "vehicleTypeId":int(vehicleTypeId),
                        "regions":[

                        ],
                        "parkName":parkname,
                        "ruleIntervalVo":{
                            "dayMaxChargeTotal":"-1.00",
                            "maxCharge":"-1.00",
                            "ruleDurations":[

                            ],
                            "chargeType":1,
                            "chargeWay":2,
                            "dayMaxCharge":"-1.00",
                            "ruleIntervals":[
                                {
                                    "intervalMaxCharge":0.02,
                                    "dayPartingId":ID,
                                    "ruleDurations":[
                                        {
                                            "chargeStart":0,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "chargeEnd":60,
                                            "id":3281,
                                            "isRecharge":False,
                                            "scaleFee":0.03,
                                            "scaleTimes":60
                                        },
                                        {
                                            "chargeStart":60,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "id":3282,
                                            "isRecharge":False,
                                            "scaleFee":0.02,
                                            "scaleTimes":60
                                        }
                                    ],
                                    "startTime":"00:00:00",
                                    "endTime":"23:59:59",
                                    "id":RID,
                                    "scaleFee":0.03,
                                    "scaleTimes":60
                                }
                            ]
                        },
                        "parkId":int(parkid),
                        "freeTimes":30,
                        "createBy":user,
                        "createTime":"2021-07-22 17:23:03",
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "id":ID,
                        "state":1,
                        "vehicleTypeName":"小车",
                        "serviceTypeCode":-1,
                        "maxCharge":"0.12",
                        "dayMaxCharge":-1,
                        "dayMaxChargeTotal":-1,
                        "payoutValidity":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "intervalMaxCharge":"0.15",
                                "dayPartingId":ID,
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "id":RID,
                                "scaleFee":0.03,
                                "scaleTimes":60,
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":60,
                                        "scaleTimes":60,
                                        "scaleFee":0.03
                                    },
                                    {
                                        "chargeStart":60,
                                        "ruleIntervalId":RID,
                                        "dayPartingId":ID,
                                        "id":3282,
                                        "isRecharge":False,
                                        "scaleFee":0.02,
                                        "scaleTimes":60
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    dura_data_two = get_zong_xls(duration_list_values,duration_list_datas,14,16)
    dura_data_data_two = list(dura_data_two)
    @data(*dura_data_data_two)
    @unpack
    def test12(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":curChannelId,
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":regionId,
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":vehicleType,
                    "agentId":agentId,
                    "parkId":parkId
                }
        self.log_port_zong(datatest)
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)

    '''
    设置单次限制小于首段时长
    '''
    @data(*dura_charge_upone_data)
    @unpack
    def test13_charge_update(self,head,parkid,parkname,vehicleTypeId,user,grammar,grammars,url):#修改计费规则—增加时段最高
        self.log_port_zong(head)
        idv = self.mysql_zong(grammar=grammar)
        ID = idv[0][0]
        rid = self.mysql_zong(grammar=grammars)
        RID = rid[0][0]
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "vehicleTypeId":int(vehicleTypeId),
                        "regions":[

                        ],
                        "parkName":parkname,
                        "ruleIntervalVo":{
                            "dayMaxChargeTotal":"-1.00",
                            "maxCharge":"0.12",
                            "ruleDurations":[

                            ],
                            "chargeType":1,
                            "chargeWay":2,
                            "dayMaxCharge":"-1.00",
                            "ruleIntervals":[
                                {
                                    "intervalMaxCharge":0.15,
                                    "dayPartingId":ID,
                                    "ruleDurations":[
                                        {
                                            "chargeStart":0,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "chargeEnd":60,
                                            "id":3283,
                                            "isRecharge":False,
                                            "scaleFee":0.03,
                                            "scaleTimes":60
                                        },
                                        {
                                            "chargeStart":60,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "id":3284,
                                            "isRecharge":False,
                                            "scaleFee":0.02,
                                            "scaleTimes":60
                                        }
                                    ],
                                    "startTime":"00:00:00",
                                    "endTime":"23:59:59",
                                    "id":RID,
                                    "scaleFee":0.03,
                                    "scaleTimes":60
                                }
                            ]
                        },
                        "parkId":int(parkid),
                        "freeTimes":30,
                        "createBy":user,
                        "createTime":"2021-07-22 17:23:03",
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "id":ID,
                        "state":1,
                        "vehicleTypeName":"小车",
                        "serviceTypeCode":-1,
                        "maxCharge":"0.02",
                        "dayMaxCharge":-1,
                        "dayMaxChargeTotal":-1,
                        "payoutValidity":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "intervalMaxCharge":"0",
                                "dayPartingId":ID,
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "id":RID,
                                "scaleFee":0.03,
                                "scaleTimes":60,
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":60,
                                        "scaleTimes":60,
                                        "scaleFee":0.03
                                    },
                                    {
                                        "chargeStart":60,
                                        "ruleIntervalId":RID,
                                        "dayPartingId":ID,
                                        "id":3284,
                                        "isRecharge":False,
                                        "scaleFee":0.02,
                                        "scaleTimes":60
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    dura_data_two = get_zong_xls(duration_list_values,duration_list_datas,17,19)
    dura_data_data_two = list(dura_data_two)
    @data(*dura_data_data_two)
    @unpack
    def test14(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":curChannelId,
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":regionId,
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":vehicleType,
                    "agentId":agentId,
                    "parkId":parkId
                }
        self.log_port_zong(datatest)
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)


    '''
    设置单次限制大于时段最高费用
    '''
    @data(*dura_charge_upone_data)
    @unpack
    def test15_charge_update(self,head,parkid,parkname,vehicleTypeId,user,grammar,grammars,url):#修改计费规则—增加时段最高
        self.log_port_zong(head)
        idv = self.mysql_zong(grammar=grammar)
        ID = idv[0][0]
        rid = self.mysql_zong(grammar=grammars)
        RID = rid[0][0]
        #datatest = eval(postdata)
        datatest = {
                    "chargingWay":3,
                    "tempChargingDuration":{
                        "vehicleTypeId":int(vehicleTypeId),
                        "regions":[

                        ],
                        "parkName":parkname,
                        "ruleIntervalVo":{
                            "dayMaxChargeTotal":"-1.00",
                            "maxCharge":"0.02",
                            "ruleDurations":[

                            ],
                            "chargeType":1,
                            "chargeWay":2,
                            "dayMaxCharge":"-1.00",
                            "ruleIntervals":[
                                {
                                    "intervalMaxCharge":0,
                                    "dayPartingId":ID,
                                    "ruleDurations":[
                                        {
                                            "chargeStart":0,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "chargeEnd":60,
                                            "id":3285,
                                            "isRecharge":False,
                                            "scaleFee":0.03,
                                            "scaleTimes":60
                                        },
                                        {
                                            "chargeStart":60,
                                            "ruleIntervalId":RID,
                                            "dayPartingId":ID,
                                            "id":3286,
                                            "isRecharge":False,
                                            "scaleFee":0.02,
                                            "scaleTimes":60
                                        }
                                    ],
                                    "startTime":"00:00:00",
                                    "endTime":"23:59:59",
                                    "id":RID,
                                    "scaleFee":0.03,
                                    "scaleTimes":60
                                }
                            ]
                        },
                        "parkId":int(parkid),
                        "freeTimes":30,
                        "createBy":user,
                        "createTime":"2021-07-22 17:23:03",
                        "chargingWay":3,
                        "ruleName":"按停车时长间隔小车",
                        "id":ID,
                        "state":1,
                        "vehicleTypeName":"小车",
                        "serviceTypeCode":-1,
                        "maxCharge":"0.15",
                        "dayMaxCharge":-1,
                        "dayMaxChargeTotal":-1,
                        "payoutValidity":-1,
                        "tempChargingIntervalDetailList":[
                            {
                                "intervalMaxCharge":"0.12",
                                "dayPartingId":ID,
                                "startTime":"00:00:00",
                                "endTime":"23:59:59",
                                "id":RID,
                                "scaleFee":0.03,
                                "scaleTimes":60,
                                "tempChargingDurationDetailList":[
                                    {
                                        "chargeStart":"0",
                                        "chargeEnd":60,
                                        "scaleTimes":60,
                                        "scaleFee":0.03
                                    },
                                    {
                                        "chargeStart":60,
                                        "ruleIntervalId":RID,
                                        "dayPartingId":ID,
                                        "id":3286,
                                        "isRecharge":False,
                                        "scaleFee":0.02,
                                        "scaleTimes":60
                                    }
                                ]
                            }
                        ],
                        "tempChargingDurationDetailList":[
                            {
                                "chargeStart":1440
                            }
                        ]
                    }
                }
        url_path=url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        print(self.res)
        self.assertEqual(self.res['code'],200)

    dura_data_two = get_zong_xls(duration_list_values,duration_list_datas,20,23)
    dura_data_data_two = list(dura_data_two)
    @data(*dura_data_data_two)
    @unpack
    def test16(self,head,curChannelId,plate,enterTime,regionId,exitDate,vehicleType,agentId,parkId,url,verify):#车辆进出场
        self.log_port_zong(head)
        #datatest = eval(postdata)
        datatest = {
                    "curChannelId":curChannelId,
                    "plate":plate,
                    "accessList":[
                        {
                            "enterTime":enterTime,
                            "regionId":regionId,
                            "orderSerial":"1232354363457234247634"
                        }
                    ],
                    "exitDate":exitDate,
                    "vehicleType":vehicleType,
                    "agentId":agentId,
                    "parkId":parkId
                }
        self.log_port_zong(datatest)
        url_path = url
        self.res = self.request.SendRequest(method='POST',url=url_path,json=datatest)
        self.assertEqual(self.res['fee'],verify,msg='计费错误')
        self.log_port_zong('计算正确')
        self.log_port_zong(verify)



'''
    # dura_service_del = get_zong_xls(duration_list_values,duration_list_service_del,1,2)
    # dura_service_del_data = list(dura_service_del)
    # @data(*dura_service_del_data)
    # @unpack
    # def test09(self,head,grammar,url):#删除服务车辆
    #     self.log_port_zong(head)
    #     idc = self.mysql_zong(grammar=grammar)
    #     for i in idc:
    #         url_path = url+str(i[0])
    #         print(url_path)
    #         self.res = self.request.SendRequest(method='get',url=url_path)
    #         self.assertEqual(self.res['code'],200)
    #
    #
    # dure_charge_del = get_zong_xls(duration_list_values,duration_list_charge_del,1,2)
    # dure_charge_del_data = list(dure_charge_del)
    # @data(*dure_charge_del_data)
    # @unpack
    # def test10(self,head,grammar,url,chargingWay):#删除计费规则
    #     self.log_port_zong(head)
    #     idv = self.mysql_zong(grammar=grammar)
    #     date = [{"id":idv[0][0],"chargingWay":chargingWay}]
    #     url_path = url
    #     self.res = self.request.SendRequest(method='post',url=url_path,json=date)
    #     self.assertEqual(self.res['code'],200)
    #     print(self.res)
'''
    # def tearDownClass(self) -> None:
    #     pass

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    zong_list = [Charg_Zong]
    for i in zong_list:
        cases = loader.loadTestsFromTestCase(i)
        suite.addTest(cases)
    runner = HTMLTestRunner(stream=open('login_report.html','wb'),
                   verbosity=2,
                   title='纵停车接口自动化测试报告',
                   description='纵停车计费接口自动化测试',
                   tester='谢港')
    runner.run(suite)

