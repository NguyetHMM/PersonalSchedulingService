from importlib_metadata import NullFinder
from sqlalchemy import null


result =  [
        {
            "end_time": "2021-11-15 08:00:00",
            "id": "75099ffb-c57e-4364-b6dc-add6897ff88f",
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-19 17:00:00",
            "id": "7e2b4a2a-fe67-45e3-86ad-111e54ce0da7",
            "start_time": "2021-11-19 17:00:00"
        },
        {
            "end_time": "2021-11-15 13:00:00",
            "id": "1",
            "start_time": "2021-11-15 12:00:00"
        },
        {
            "end_time": "2021-11-16 13:00:00",
            "id": "2",
            "start_time": "2021-11-15 17:00:00"
        },
        {
            "end_time": "2021-11-15 21:00:00",
            "id": "3",
            "start_time": "2021-11-15 20:00:00"
        },
        {
            "end_time": "2021-11-16 06:45:00",
            "id": "4",
            "start_time": "2021-11-15 23:00:00"
        },
        {
            "end_time": "2021-11-16 13:00:00",
            "id": "5",
            "start_time": "2021-11-16 12:00:00"
        },
        {
            "end_time": "2021-11-16 21:00:00",
            "id": "6",
            "start_time": "2021-11-16 17:00:00"
        },
        {
            "end_time": "2021-11-16 21:00:00",
            "id": "7",
            "start_time": "2021-11-16 20:00:00"
        },
        {
            "end_time": "2021-11-17 08:15:00",
            "id": "8",
            "start_time": "2021-11-16 23:00:00"
        },
        {
            "end_time": "2021-11-17 13:00:00",
            "id": "9",
            "start_time": "2021-11-17 12:00:00"
        },
        {
            "end_time": "2021-11-18 08:00:00",
            "id": "10",
            "start_time": "2021-11-17 17:00:00"
        },
        {
            "end_time": "2021-11-18 08:00:00",
            "id": "11",
            "start_time": "2021-11-17 23:00:00"
        },
        {
            "end_time": "2021-11-18 13:00:00",
            "id": "12",
            "start_time": "2021-11-18 12:00:00"
        },
        {
            "end_time": "2021-11-18 20:00:00",
            "id": "13",
            "start_time": "2021-11-18 17:00:00"
        },
        {
            "end_time": "2021-11-15 20:00:00",
            "id": "f2ecc105-8313-48ff-bb9b-c361d4f3d506",
            "job": {
                "early_start_time": "2021-11-15 18:00:00",
                "estimated_time": 120,
                "finish_time": null,
                "flextime": 0,
                "id": "1",
                "late_finish_time": "2021-11-15 20:00:00",
                "name": "Nhật NetK",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-15 18:00:00"
        },
        {
            "end_time": "2021-11-16 20:00:00",
            "id": "28c7b30d-78c3-4ce8-96dd-110770b58b05",
            "job": {
                "early_start_time": "2021-11-16 18:00:00",
                "estimated_time": 120,
                "finish_time": null,
                "flextime": 0,
                "id": "2",
                "late_finish_time": "2021-11-16 20:00:00",
                "name": "Nhật NetK",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-16 18:00:00"
        },
        {
            "end_time": "2021-11-18 20:00:00",
            "id": "c41a5403-6cb7-4cd5-8625-56b4ca0f7ede",
            "job": {
                "early_start_time": "2021-11-18 18:00:00",
                "estimated_time": 120,
                "finish_time": null,
                "flextime": 0,
                "id": "3",
                "late_finish_time": "2021-11-18 20:00:00",
                "name": "Nhật NetK",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 18:00:00"
        },
        {
            "end_time": "2021-11-16 08:15:00",
            "id": "4abc9bcf-bed6-4485-a324-135a44058109",
            "job": {
                "early_start_time": "2021-11-16 06:45:00",
                "estimated_time": 90,
                "finish_time": null,
                "flextime": 0,
                "id": "4",
                "late_finish_time": "2021-11-16 08:15:00",
                "name": "Mạng Internet",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-16 06:45:00"
        },
        {
            "end_time": "2021-11-16 11:45:00",
            "id": "421a3e17-5b27-4b9d-81e0-3fadcfafc984",
            "job": {
                "early_start_time": "2021-11-16 08:25:00",
                "estimated_time": 200,
                "finish_time": null,
                "flextime": 0,
                "id": "5",
                "late_finish_time": "2021-11-16 11:45:00",
                "name": "ITSS 2",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-16 08:25:00"
        },
        {
            "end_time": "2021-11-17 08:15:00",
            "id": "56d7800a-f173-4187-855f-e1989f0e3855",
            "job": {
                "early_start_time": "2021-11-17 06:45:00",
                "estimated_time": 90,
                "finish_time": null,
                "flextime": 0,
                "id": "6",
                "late_finish_time": "2021-11-17 08:15:00",
                "name": "Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 06:45:00"
        },
        {
            "end_time": "2021-11-17 13:00:00",
            "id": "d45f0c4d-d457-40f7-ab6e-279e38f677aa",
            "job": {
                "early_start_time": "2021-11-17 10:15:00",
                "estimated_time": 90,
                "finish_time": null,
                "flextime": 0,
                "id": "7",
                "late_finish_time": "2021-11-17 11:45:00",
                "name": "Knowledge Engineering",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 10:15:00"
        },
        {
            "end_time": "2021-11-15 23:00:00",
            "id": "0c215308-634f-4ff5-97df-5fa31ddcf6aa",
            "job": {
                "early_start_time": "2021-11-15 21:00:00",
                "estimated_time": 120,
                "finish_time": null,
                "flextime": 0,
                "id": "8",
                "late_finish_time": "2021-11-15 23:00:00",
                "name": "Họp ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-15 21:00:00"
        },
        {
            "end_time": "2021-11-17 23:00:00",
            "id": "de1b01ed-530c-47f3-8465-cea266cd25e7",
            "job": {
                "early_start_time": "2021-11-17 20:30:00",
                "estimated_time": 150,
                "finish_time": null,
                "flextime": 0,
                "id": "9",
                "late_finish_time": "2021-11-17 23:00:00",
                "name": "Báo cáo GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 20:30:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "3c1bdaf6-58b3-4e83-ac07-5a8bf9fbcc83",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 690,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "c10830b8-ad90-48b9-9e5a-0ab6ef7fc87f",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 450,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "0875c27c-c818-408b-9db2-f3c7a67a6c63",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 210,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "aa3234bc-234f-496f-9845-e5a64406685d",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 09:45:00",
            "id": "32101129-743e-4c75-a162-8039306b90f9",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-17 10:15:00",
            "id": "659d6940-ad7a-44d9-938c-58ffa15daf3f",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 30,
            "start_time": "2021-11-17 09:45:00"
        },
        {
            "end_time": "2021-11-17 13:30:00",
            "id": "80483a8e-f541-47e6-bca6-b8ef153d28b0",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 13:00:00"
        },
        {
            "end_time": "2021-11-17 17:00:00",
            "id": "d2444567-e8ef-4ed5-9008-9ecd1f23d060",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 630,
            "start_time": "2021-11-17 13:30:00"
        },
        {
            "end_time": "2021-11-18 12:00:00",
            "id": "63a4123e-5614-4194-9ffb-51509d0b6784",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 390,
            "start_time": "2021-11-18 08:00:00"
        },
        {
            "end_time": "2021-11-18 17:00:00",
            "id": "d9b58d04-7077-4db8-ab1d-3dcd3f76edf8",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 150,
            "start_time": "2021-11-18 13:00:00"
        },
        {
            "end_time": "2021-11-18 22:30:00",
            "id": "14ef6621-a640-4fbf-aa31-61018c669a39",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 20:00:00"
        },
        {
            "end_time": "2021-11-19 05:30:00",
            "id": "c5172e86-3420-453f-b873-61aee870dc2a",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 22:30:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "20bdf454-6407-4c4a-a929-5e951ce1c705",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 180,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 16:00:00",
            "id": "5d0952b4-cccc-48fc-bbf9-2961fc7906aa",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "e3dd304d-0cc8-4ccc-9d8a-df3e0edba5d6",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 780,
            "start_time": "2021-11-15 16:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "b970551c-a40e-4983-bd58-5f3ea3c3db98",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 540,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "761d52b5-5d4f-4de3-aab3-6e2ff7e9ec55",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 420,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 10:15:00",
            "id": "d214898a-3510-4c6d-86ea-2b95b6dc312d",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 300,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-17 17:00:00",
            "id": "60394e2b-db49-4308-bcf7-cbd24edcd34d",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 60,
            "start_time": "2021-11-17 13:00:00"
        },
        {
            "end_time": "2021-11-18 09:00:00",
            "id": "1895097a-c0fa-4d44-b511-c4c5126ba07b",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 08:00:00"
        },
        {
            "end_time": "2021-11-18 10:00:00",
            "id": "6dd22c38-fb19-4096-a842-0da71361a3f0",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 09:00:00"
        },
        {
            "end_time": "2021-11-18 12:00:00",
            "id": "ba452459-c36f-465b-9e00-87ae9c685eed",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 810,
            "start_time": "2021-11-18 10:00:00"
        },
        {
            "end_time": "2021-11-18 17:00:00",
            "id": "a786a251-55d7-4788-a9b5-bfd7d5ba2637",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 570,
            "start_time": "2021-11-18 13:00:00"
        },
        {
            "end_time": "2021-11-19 05:30:00",
            "id": "6a48fa6e-bbc3-49c7-b137-c6ee83f28002",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 20:00:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "2bd61911-83ea-4a2a-8308-3e128329fa00",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 690,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "f033f3b5-ac9e-441c-9922-0bfa5b4741b8",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 450,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "0406ba24-556a-40b2-9f22-2790185ee960",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 210,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "288d3aef-f69a-464b-b980-ad9593a496c8",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 09:45:00",
            "id": "5a5e7f45-d397-4141-b7c1-a5a0c0bb2690",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-17 10:15:00",
            "id": "3f5ebfec-c90e-4582-88f0-a7cef91dd8ea",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 390,
            "start_time": "2021-11-17 09:45:00"
        },
        {
            "end_time": "2021-11-17 17:00:00",
            "id": "cc904213-bc1d-4a18-ae5e-9d6fe3f92f72",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 150,
            "start_time": "2021-11-17 13:00:00"
        },
        {
            "end_time": "2021-11-18 10:30:00",
            "id": "5d0b9352-e344-4fca-893b-c597ae28d463",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 08:00:00"
        },
        {
            "end_time": "2021-11-18 12:00:00",
            "id": "43b1e2bf-cad7-49c9-8a85-c8835f37225e",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 750,
            "start_time": "2021-11-18 10:30:00"
        },
        {
            "end_time": "2021-11-18 17:00:00",
            "id": "f33b93f1-fa49-4963-8d4e-b34abbee47f7",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 510,
            "start_time": "2021-11-18 13:00:00"
        },
        {
            "end_time": "2021-11-19 04:30:00",
            "id": "dcbc8a76-7074-4929-826a-18c2ed1c717b",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 20:00:00"
        },
        {
            "end_time": "2021-11-19 05:30:00",
            "id": "7fbbe5b6-1d2a-4f64-98f1-fee388e9c236",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-19 04:30:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "a5ad8ec9-ff2b-4f4d-a9c4-0c8d5accd32c",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 600,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "840e272f-918b-42bb-be91-662e7065f2a2",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 360,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "123872e0-ab95-49d2-886b-b8aefef38c7f",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 120,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "1e8b55cd-6309-4849-abf0-111282ec01d5",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 10:15:00",
            "id": "5da2d7b2-ab57-4d96-a60e-6c685b67e98a",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 810,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-17 17:00:00",
            "id": "8828a457-27c1-4b4a-9ad2-f31a0f34f304",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 570,
            "start_time": "2021-11-17 13:00:00"
        },
        {
            "end_time": "2021-11-18 12:00:00",
            "id": "9916f13a-df9a-4605-bd87-487383d3a5df",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 330,
            "start_time": "2021-11-18 08:00:00"
        },
        {
            "end_time": "2021-11-18 17:00:00",
            "id": "3ab39159-cad5-4a0d-aa7f-500431375d11",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-18 13:00:00"
        },
        {
            "end_time": "2021-11-18 21:30:00",
            "id": "4ae5ca01-57c6-4528-8181-e02b15016711",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 20:00:00"
        },
        {
            "end_time": "2021-11-18 22:30:00",
            "id": "7261bdc0-d0df-4ef8-aeb4-6fd585138808",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 21:30:00"
        },
        {
            "end_time": "2021-11-19 05:30:00",
            "id": "a0cc7d10-6921-4b27-bb63-62753fac380f",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 22:30:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "2ab05fb3-db6b-4218-9580-8ba933b333e0",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 690,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "2e2f10ce-baa3-4415-a51c-b0458d650e31",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 450,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "7642e85b-9178-47de-9ec1-f025f2b431f5",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 210,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "7a52a22a-c34b-4ad5-b2b5-5e2b923719a3",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 09:45:00",
            "id": "246c774d-318c-4447-98fb-0e77b62da0ee",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-17 10:15:00",
            "id": "2b6144c4-ca05-45e5-9716-bad8eccb9cee",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 390,
            "start_time": "2021-11-17 09:45:00"
        },
        {
            "end_time": "2021-11-17 17:00:00",
            "id": "83a48e46-6450-40de-9146-d2e438a3c6ba",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 150,
            "start_time": "2021-11-17 13:00:00"
        },
        {
            "end_time": "2021-11-18 10:30:00",
            "id": "92b6f143-7a39-481d-8c60-27a016b76337",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 08:00:00"
        },
        {
            "end_time": "2021-11-18 12:00:00",
            "id": "437685f0-21d7-42d4-8720-40a641e5e1cb",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 750,
            "start_time": "2021-11-18 10:30:00"
        },
        {
            "end_time": "2021-11-18 17:00:00",
            "id": "0fc69235-d98f-4398-b078-a4bd1dfcd7f0",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 510,
            "start_time": "2021-11-18 13:00:00"
        },
        {
            "end_time": "2021-11-19 04:30:00",
            "id": "5ec4e92d-6238-4c61-930b-37f21bb69579",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 20:00:00"
        },
        {
            "end_time": "2021-11-19 05:30:00",
            "id": "3d10fa2e-bb6e-4f07-baed-55c1fb793bf4",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-19 04:30:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "5346479b-4721-4453-a561-d684651500a3",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 600,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "283680bb-f379-4caf-9872-93289ae48e1d",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 360,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "c83b4dc1-574c-4c75-9cab-3d211c498430",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 120,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "c43a4709-5e35-4f6c-b673-1ef9e3d04935",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "5edb0574-ff4a-4ff4-b988-efe3ead9e324",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 690,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "98ebbc67-4a65-42b8-9317-5801166dbbb1",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 450,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "d4a67a4d-1cf1-4011-bf01-981104581cd8",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 210,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "24efc3ad-598e-4052-b3cc-58f597f97e76",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 09:45:00",
            "id": "6bdb5bdf-4341-4555-8f05-91e86a86c6e1",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-15 12:00:00",
            "id": "9d4dd231-4505-4353-9591-0537c64190f9",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 690,
            "start_time": "2021-11-15 08:00:00"
        },
        {
            "end_time": "2021-11-15 17:00:00",
            "id": "b25e4440-f929-4f17-8ad6-9ac3a7472681",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 450,
            "start_time": "2021-11-15 13:00:00"
        },
        {
            "end_time": "2021-11-16 17:00:00",
            "id": "7f81ef4b-792c-4f6d-9dff-568ad47fd70f",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 210,
            "start_time": "2021-11-16 13:00:00"
        },
        {
            "end_time": "2021-11-16 23:00:00",
            "id": "421be039-aa9e-4844-8c73-ac37b3dff02d",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-16 21:00:00"
        },
        {
            "end_time": "2021-11-17 09:45:00",
            "id": "11016cac-34e3-41ff-ae16-c521e754a2b8",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 930,
                "finish_time": null,
                "flextime": 1,
                "id": "12",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Thuật toán GR",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-17 08:15:00"
        },
        {
            "end_time": "2021-11-17 10:15:00",
            "id": "1da08ab3-2a2a-48c1-81f6-4a18b33f7ac3",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 810,
            "start_time": "2021-11-17 09:45:00"
        },
        {
            "end_time": "2021-11-17 17:00:00",
            "id": "2a07134f-bdd5-44cf-b54a-25b4d6a397b7",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 570,
            "start_time": "2021-11-17 13:00:00"
        },
        {
            "end_time": "2021-11-18 12:00:00",
            "id": "8520ef57-02cf-4ab9-971b-15a5a2ce3139",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 330,
            "start_time": "2021-11-18 08:00:00"
        },
        {
            "end_time": "2021-11-18 17:00:00",
            "id": "50fef082-8722-48e8-a2eb-d1bf3565ae01",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 90,
            "start_time": "2021-11-18 13:00:00"
        },
        {
            "end_time": "2021-11-18 21:30:00",
            "id": "b2110aff-966c-4625-b1b0-b52b2e7f09d9",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 840,
                "finish_time": null,
                "flextime": 1,
                "id": "13",
                "late_finish_time": "2021-11-19 17:00:00",
                "name": "Knowledge Engineering Project",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 20:00:00"
        },
        {
            "end_time": "2021-11-18 22:30:00",
            "id": "8fbdecb6-4f63-4633-9c69-728517351727",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 60,
                "finish_time": null,
                "flextime": 1,
                "id": "10",
                "late_finish_time": "2021-11-15 21:00:00",
                "name": "Script ITSS",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 21:30:00"
        },
        {
            "end_time": "2021-11-19 05:30:00",
            "id": "95a2390b-5d5e-4dd7-9aa7-e257a1c3ffab",
            "job": {
                "early_start_time": "2021-11-15 08:00:00",
                "estimated_time": 420,
                "finish_time": null,
                "flextime": 1,
                "id": "11",
                "late_finish_time": "2021-11-17 06:45:00",
                "name": "Ôn tập Realtime System",
                "start_time": null
            },
            "remaining_time": 0,
            "start_time": "2021-11-18 22:30:00"
        }
    ]
result.sort(key=lambda x: x['start_time'])
for re in result:
    print(re)
# print(result)
