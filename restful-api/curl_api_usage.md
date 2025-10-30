# Using curl to Interact with APIs

## 1. Verify curl Installation
To check if **curl** is installed on your system, run:
```bash
curl --version
```
**Expected Output:** Version information and supported protocols for curl.

---

## 2. Retrieve a Web Page
Use curl to download a basic web page:
```bash
curl http://example.com
```
**Expected Output:** The raw HTML content of the specified website.

---

## 3. Retrieve Data from JSONPlaceholder API
Fetch sample post data from the public JSONPlaceholder API:
```bash
curl https://jsonplaceholder.typicode.com/posts
```
**Expected Output:** A JSON array of posts containing fields such as `userId`, `id`, `title`, and `body`.

---

## 4. View Only HTTP Headers
Use the `-I` (uppercase i) option to display only the HTTP response headers:
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```
**Expected Output:** HTTP status line and headers like `Content-Type`, `Content-Length`, and others.

---

## 5. Send a POST Request
To send data to a server, specify the method with `-X` and include data with `-d`:
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
**Expected Output:** A simulated JSON response representing the newly created post, typically including an `id` of 101.

---

## Additional Notes
- If you have **jq** installed, you can format JSON output for better readability:
```bash
curl https://jsonplaceholder.typicode.com/posts | jq
```
- **JSONPlaceholder** is a free fake REST API commonly used for testing and prototyping applications.
