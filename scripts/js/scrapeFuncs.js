const puppeteer = require("puppeteer");
const fs = require("fs");


/**
 * async func that scrapes course data between 1 state school and 1 cc w/ Puppeteer
 * @param {Browser} browser  the browser instance
 * @param {string} url  the assist url to scrape
 * @returns {Promise<Object>}  promise that resolves scraped data
 */
async function scrapeURL(browser, url) {
    const page = await browser.newPage();
    await page.goto(url);

    console.log("Checking for articulation data...")  // this try block limiting factor
    try {
        await page.waitForSelector('.rowReceiving', { visible: true });
        await page.waitForSelector('.rowSending', { visible: true });
    } catch (error) {
        throw Error("No courses found!")
    }
    console.log("Articulation data found")

    const stateCourses = await getCourses('.rowReceiving', page);
    // const ccCourses = await getCourses('.rowSending', page);
    page.close();
}

/**
 * helper function for scrapeURL
 * async func that grabs and cleans the actual text from the given css element
 * on a given puppeteer page object & returns it
 * @param {string} cssSelector
 * @param {puppeteer.Page} page 
 * @returns {Promise<String[]>} an array of cleaned courses + descriptions
 */
async function getCourses(cssSelector, page) {
    console.log(page.url());
    await page.$$eval('.rowReceiving', element => element.map(element => {
        console.log("eval")
        const text = element.textContent?.trim();
        console.log(text);
        // TODO: add logic for cleaning course data
    }));
}



module.exports = { scrapeURL, getCourses };