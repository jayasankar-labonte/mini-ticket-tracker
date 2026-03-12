import { test, expect } from '@playwright/test';

test('create ticket flow', async ({ page }) => {

  await page.goto('http://localhost:3000');

  await page.click('text=New Ticket');

  await page.fill('input[name="title"]', 'Playwright Ticket');

  await page.fill('textarea[name="description"]', 'Testing E2E');

  await page.click('text=Save Ticket');

  await expect(page.locator('text=Playwright Ticket')).toBeVisible();

});