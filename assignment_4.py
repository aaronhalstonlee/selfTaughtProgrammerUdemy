import csv

with open("assn4.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow([
        "Top Gun",
        "Risky Business",
        "Minority Report"
        ])
    write.writerow([
        "Titanic",
        "The Revenant",
        "Inception"
        ])
    write.writerow([
        "Training Day",
        "Man on Fire",
        "Flight"
        ])
