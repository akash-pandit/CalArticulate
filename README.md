## Current Issues & TBDs
issues:
- figure out why getCourses() in scrapeFuncs.js no no worky

tbds -> db finished:
- finish dockerfiles for js & python
- create docker-compose.yml to manage dockerfile image exec
- write unit tests for js & python scripts
- setup & learn how to use firebase firestore w/ js

## File Structure & Descriptions

CalArticulate/                          root
│
├── app/                                actual web app code, tbd
│
├── data/
│   ├── assist_urls.json                maps list of agreement urls to state unis
│   ├── institutions_cc.json            maps url id to name for ccs
│   └── institutions_state.json         maps url id to name for state unis
│
├── node_modules/                       self explanatory
│
├── scripts/                            contains scripts for creating db
│   ├── js/                             js scripts for db generation
│   │   ├── Dockerfile                  dockerfile for running js scripts & tests & populating db
│   │   ├── scrapeFuncs.js              utility funcs for scrapeURLsMain.json
│   │   └── scrapeURLsMain.js           in: data/assist_urls.json, out: TBD
│   └── python/                         python scripts for db generation
│       ├── Dockerfile                  dockerfile for running python scripts & generating jsons
│       ├── gen_institutions.py         out: data/institutions_*.json
│       └── gen_urls.py                 in: data/institutions_*.json, out: data/assist_urls.json
│
├── tests/                              testing 
│   ├── js/                             js tests, WIP
│   │   ├── scrapeURLs.test.js          unit tests for scrapeFuncs.js
│   │   └── test_course_data.html       test data for scrapeURLs.test.js
│   └── python/                         python tests, TBD
│
├── LICENSE                             GPL 2.0 License
├── package-lock.json                   npm-generated exact package record
├── package.json                        define project metadata & dependencies
└── README.md                           You Are Here, currently visualizes & explains proj file structure