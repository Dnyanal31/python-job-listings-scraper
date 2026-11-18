import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_data = []

for job in jobs:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")

    link = job.find_next("a", string="Apply")

    if title and company and location:
        job_title = title.text.strip()
        company_name = company.text.strip()
        job_location = location.text.strip()
        job_url = link["href"] if link else "Not available"

        job_data.append([job_title, company_name, job_location, job_url])

with open("job_listings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Job Title", "Company Name", "Location", "Job URL"])

    writer.writerows(job_data)

print("Scraping completed!")
print("Total jobs collected:", len(job_data))
print("Data saved in job_listings.csv")
