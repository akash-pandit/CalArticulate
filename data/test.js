import puppeteer from "puppeteer";
import urlsBy4yr from './assist_urls.json';  // '4yr' == 'state school'

/**
 * async func that scrapes course data between 1 state school and 1 cc w/ Puppeteer
 * @param {Browser} browser  the browser instance
 * @param {String} url  the assist url to scrape
 * @returns {Promise<Object>}  promise that resolves scraped data
 */
async function scrapeURL(browser, url) {
    const page = await browser.newPage();
    await browser.goto(url);

    console.log("Checking for articulation data...")
    try {
        await page.waitForSelector('.rowReceiving', { visible: true });
        await page.waitForSelector('.rowSending', { visible: true });
    } catch (error) {
        throw Error("No courses found!")
    }
    console.log("Articulation data found")

    const stateCourses = await getCourses('.rowReceiving');
    const ccCourses = await getCourses('.rowSending');
}

/**
 * helper function for scrapeURL
 * async func that grabs and cleans the actual text from the given css element
 * on a given puppeteer page object & returns it
 * @param {String} cssSelector
 * @param {puppeteer.Page} page 
 * @returns {Promise<String[]>} an array of cleaned courses + descriptions
 */
async function getCourses(cssSelector, page) {
    await page.$$eval('.rowReceiving', element => element.map(element => {
        const text = element.textContent?.trim();
        
        // TODO: add logic for cleaning course data
    }));
}

// "main" function
(async () => {
    Object.keys(urlsBy4yr).forEach(stateID => {
        console.log(stateID);
    });
});