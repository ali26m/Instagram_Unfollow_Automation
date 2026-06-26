from bs4 import BeautifulSoup

# Input and output files
input_file = "data/instagram/pending_follow_requests.html"
output_file = "data/instagram/pending_usernames_requests.html"

# Read HTML
with open(input_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all table rows
for row in soup.find_all("tr"):
    cells = row.find_all("td")

    # Ensure there are exactly two columns
    if len(cells) == 2:
        label = cells[0].get_text(strip=True)

        # Look for the Username row
        if label == "Username":
            username_cell = cells[1]
            username = username_cell.get_text(strip=True)

            # Create hyperlink
            link = soup.new_tag(
                "a",
                href=f"https://www.instagram.com/{username}",
                target="_blank",
                
            )
            link.string = f"https://www.instagram.com/{username}"

            # Replace existing text
            username_cell.clear()
            username_cell.append(link)

# Save modified HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"Saved modified HTML to {output_file}")