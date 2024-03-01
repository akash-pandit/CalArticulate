const urlsBy4yr = require("../../data/assist_urls.json");
const puppeteer = require("puppeteer");
const { scrapeURL } = require("./scrapeFuncs.js");

(async () => {
    const browser = await puppeteer.launch({headless: 'shell', 
    args: ['--no-sandbox', '--disable-setuid-sandbox']})

    for (let stateID of Object.keys(urlsBy4yr)) {

        for (let url of urlsBy4yr[stateID]) {
            await scrapeURL(browser, url)
        }
        break;  // testing on the first
    }
})();