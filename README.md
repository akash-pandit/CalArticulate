# CalArticulate

Web app for finding articulated california community college courses for a given UC/CSU course. Data sourced from ASSIST.org. TBD!

While ASSIST is great when it comes to mapping programs between unis and ccs or even transferrable courses by community college, looking for transferrable courses by university course across several CCs is a *huge* pain. 

That's what this project plans to address!

## Current Issues & TBDs
issues:
- figure out why getCourses() in scrapeFuncs.js no no worky

tbds -> db finished:
- finish dockerfiles for js & python
- create docker-compose.yml to manage dockerfile image exec
- write unit tests for js & python scripts
- setup & learn how to use firebase firestore w/ js

## File Structure & Descriptions


```
CalArticulate/                          root
│
├── app/                                actual web app code, tbd
│
├── data/
│   ├── assist_urls.json                maps list of agreement urls to state unis
│   ├── institutions_cc.json            maps url id to name for ccs
│   └── institutions_state.json         maps url id to name for state unis
│
├── node_modules/*                      self explanatory
|
├── scripts/                            contains scripts for creating db
│   ├── js/                             js scripts for db generation
|   |   ├── node_modules/*              node modules for js scripts
│   │   ├── tests/                      js tests, WIP
│   │   │   ├── scrapeURLs.test.js      unit tests for scrapeFuncs.js
│   │   │   └── test_course_data.html   test data for scrapeURLs.test.js
│   │   ├── Dockerfile                  dockerfile for running js scripts & tests & populating db
│   │   ├── package-lock.json           npm-generated exact package record
│   │   ├── package.json                define project metadata & dependencies
│   │   ├── scrapeFuncs.js              utility funcs for scrapeURLsMain.json
│   │   └── scrapeURLsMain.js           in: data/assist_urls.json, out: TBD
|   |
│   └── python/                         python scripts for db generation
|       ├── tests/                      python tests, TBD
│       ├── Dockerfile                  dockerfile for running python scripts & generating jsons
│       ├── gen_institutions.py         out: data/institutions_*.json
│       └── gen_urls.py                 in: data/institutions_*.json, out: data/assist_urls.json
│
├── LICENSE                             GPL 3.0 License
└── README.md                           You Are Here, currently visualizes & explains proj file structure
```
