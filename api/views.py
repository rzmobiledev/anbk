from requests import HTTPError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.config import MYINFO_CLIENT
from myinfo.client import MyInfoPersonalClientV4


class GetMyInfoURL(APIView):
    get_response_schema_dict = {
        "200": openapi.Response(
            description="Return a json response with with a valid url params from test.api.myinfo.gov.sg",
            examples={
                "application/json": {
                    "data": "https://test.api.myinfo.gov.sg/com/v4/authorize?client_id=STG-202327956K-ABNK-BNPLAPPLN&scope=uinfin%20name%20sex%20race%20dob%20residentialstatus%20nationality%20birthcountry%20passtype%20passstatus%20passexpirydate%20employmentsector%20mobileno%20email%20regadd%20housingtype%20hdbtype%20cpfcontributions%20noahistory%20ownerprivate%20employment%20occupation%20cpfemployers%20marital&purpose_id=7ed6f2ce&response_type=code&code_challenge=3GrrsykxwcngCtjBWowFXWJbbeiKXp4KIxHOU_OCgBA&code_challenge_method=S256&redirect_uri=http://localhost:3001/callback",
                }
            }
        ),
        "404": openapi.Response(
            description="Response 404 from test.api.myinfo.gov.sg. If you receive this, please wait for another 2(two) mins, and back access this api endpoint.",
            examples={"application/json": {
                "data": "Page not found"
            }}

        )
    }

    @swagger_auto_schema(operation_description="Retrieve a URL from https://test.api.myinfo.gov.sg with required params. Client App should open this response and access the page and return to callback page", responses=get_response_schema_dict)
    def get(self, request):
        oauth_state = MYINFO_CLIENT.get('oauth_state')
        callback_url = MYINFO_CLIENT.get('CALLBACK_URL')
        client = MyInfoPersonalClientV4()
        response = client.get_authorise_url(oauth_state, callback_url)
        if (response):
            return Response({'data': response}, status=status.HTTP_200_OK)
        return Response({'error': 'Unauthorized for url: https://test.api.myinfo.gov.sg/com/v4/token'}, status=401)


class SendMyInfoPayload(APIView):

    post_response_schema_dict = {
        "200": openapi.Response(
            description="Sample of json data returned",
            examples={
                "application/json": {
                    "data": {
                        "employmentsector": {
                            "lastupdated": "2024-01-26",
                            "source": "3",
                            "classification": "C",
                            "value": ""
                        },
                        "uinfin": {
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "classification": "C",
                            "value": "S0290695C"
                        },
                        "name": {
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "classification": "C",
                            "value": "BERNARD LI GUO HAO"
                        },
                        "sex": {
                            "lastupdated": "2024-01-26",
                            "code": "F",
                            "source": "1",
                            "classification": "C",
                            "desc": "FEMALE"
                        },
                        "race": {
                            "lastupdated": "2024-01-26",
                            "code": "CN",
                            "source": "1",
                            "classification": "C",
                            "desc": "CHINESE"
                        },
                        "dob": {
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "classification": "C",
                            "value": "1991-12-04"
                        },
                        "residentialstatus": {
                            "lastupdated": "2024-01-26",
                            "code": "P",
                            "source": "1",
                            "classification": "C",
                            "desc": "PR"
                        },
                        "nationality": {
                            "lastupdated": "2024-01-26",
                            "code": "MY",
                            "source": "1",
                            "classification": "C",
                            "desc": "MALAYSIAN"
                        },
                        "birthcountry": {
                            "lastupdated": "2024-01-26",
                            "code": "MY",
                            "source": "1",
                            "classification": "C",
                            "desc": "MALAYSIA"
                        },
                        "passtype": {
                            "lastupdated": "2024-01-26",
                            "code": "",
                            "source": "3",
                            "classification": "C",
                            "desc": ""
                        },
                        "passstatus": {
                            "lastupdated": "2024-01-26",
                            "source": "3",
                            "classification": "C",
                            "value": ""
                        },
                        "passexpirydate": {
                            "lastupdated": "2024-01-26",
                            "source": "3",
                            "classification": "C",
                            "value": ""
                        },
                        "mobileno": {
                            "lastupdated": "2024-01-26",
                            "source": "4",
                            "classification": "C",
                            "areacode": {
                                "value": "65"
                            },
                            "prefix": {
                                "value": "+"
                            },
                            "nbr": {
                                "value": "87163551"
                            }
                        },
                        "email": {
                            "lastupdated": "2024-01-26",
                            "source": "4",
                            "classification": "C",
                            "value": "dbstesting03@gmail.com"
                        },
                        "regadd": {
                            "country": {
                                "code": "SG",
                                "desc": "SINGAPORE"
                            },
                            "unit": {
                                "value": "128"
                            },
                            "street": {
                                "value": "BEDOK NORTH AVENUE 4"
                            },
                            "lastupdated": "2024-01-26",
                            "block": {
                                "value": "102"
                            },
                            "source": "1",
                            "postal": {
                                "value": "460102"
                            },
                            "classification": "C",
                            "floor": {
                                "value": "9"
                            },
                            "type": "SG",
                            "building": {
                                "value": "PEARL GARDEN"
                            }
                        },
                        "housingtype": {
                            "lastupdated": "2024-01-26",
                            "code": "131",
                            "source": "1",
                            "classification": "C",
                            "desc": "CONDOMINIUM"
                        },
                        "hdbtype": {
                            "lastupdated": "2024-01-26",
                            "code": "",
                            "source": "1",
                            "classification": "C",
                            "desc": ""
                        },
                        "cpfcontributions": {
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "history": [
                                {
                                    "date": {
                                        "value": "2022-10-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2022-10"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2022-11-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2022-11"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2022-12-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2022-12"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-01-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-01"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-02-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-02"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-03-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-03"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-04-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-04"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-05-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-05"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-06-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-06"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-07-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-07"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-08-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-08"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-09-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-09"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-10-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-10"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-11-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-11"
                                    }
                                },
                                {
                                    "date": {
                                        "value": "2023-12-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    },
                                    "amount": {
                                        "value": 2035
                                    },
                                    "month": {
                                        "value": "2023-12"
                                    }
                                }
                            ],
                            "classification": "C"
                        },
                        "noahistory": {
                            "noas": [
                                {
                                    "amount": {
                                        "value": 100000
                                    },
                                    "trade": {
                                        "value": 0
                                    },
                                    "interest": {
                                        "value": 0
                                    },
                                    "yearofassessment": {
                                        "value": "2023"
                                    },
                                    "taxclearance": {
                                        "value": "N"
                                    },
                                    "employment": {
                                        "value": 100000
                                    },
                                    "rent": {
                                        "value": 0
                                    },
                                    "category": {
                                        "value": "ORIGINAL"
                                    }
                                },
                                {
                                    "amount": {
                                        "value": 150000
                                    },
                                    "trade": {
                                        "value": 0
                                    },
                                    "interest": {
                                        "value": 0
                                    },
                                    "yearofassessment": {
                                        "value": "2022"
                                    },
                                    "taxclearance": {
                                        "value": "N"
                                    },
                                    "employment": {
                                        "value": 150000
                                    },
                                    "rent": {
                                        "value": 0
                                    },
                                    "category": {
                                        "value": "ORIGINAL"
                                    }
                                }
                            ],
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "classification": "C"
                        },
                        "ownerprivate": {
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "classification": "C",
                            "value": "false"
                        },
                        "employment": {
                            "lastupdated": "2024-01-26",
                            "source": "2",
                            "classification": "C",
                            "value": ""
                        },
                        "occupation": {
                            "lastupdated": "2024-01-26",
                            "source": "2",
                            "classification": "C",
                            "value": ""
                        },
                        "cpfemployers": {
                            "lastupdated": "2024-01-26",
                            "source": "1",
                            "history": [
                                {
                                    "month": {
                                        "value": "2022-10"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2022-11"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2022-12"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-01"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-02"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-03"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-04"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-05"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-06"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-07"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-08"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-09"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-10"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-11"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                },
                                {
                                    "month": {
                                        "value": "2023-12"
                                    },
                                    "employer": {
                                        "value": "DBS BANK LTD"
                                    }
                                }
                            ],
                            "classification": "C"
                        },
                        "marital": {
                            "lastupdated": "2024-01-26",
                            "code": "1",
                            "source": "1",
                            "classification": "C",
                            "desc": "SINGLE"
                        }
                    }
                },
            }
        )
    }

    auth_code = openapi.Parameter('auth_code', openapi.IN_PATH,
                                  description="auth_code from callback params URL PATH",
                                  type=openapi.IN_PATH)
    oauth_state = openapi.Parameter('oauth_state', openapi.IN_PATH,
                                    description="random string 16 chars length",
                                    type=openapi.IN_PATH)
    callback_url = openapi.Parameter('callback_url', openapi.IN_PATH,
                                     description="callback url",
                                     type=openapi.IN_PATH, default='http://127.0.0.1:3001/callback')

    @swagger_auto_schema(
        operation_description="Send all required params from callback page after receiving a response from api/getmyinfo/ api endpoint.",
        responses=post_response_schema_dict,
        manual_parameters=[auth_code, oauth_state, callback_url]
    )
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            auth_code = data.get('auth_code')

            oauth_state = MYINFO_CLIENT.get('oauth_state')
            callback_url = MYINFO_CLIENT.get('CALLBACK_URL')
            person_data = MyInfoPersonalClientV4().retrieve_resource(auth_code, oauth_state, callback_url)
            return Response(person_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=401)
