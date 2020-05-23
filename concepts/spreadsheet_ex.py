import gspread

# Add url of spreadsheet here
SPREADSHEET_URL = ""
OWNER_EMAIL = "exampleemail"

gc = gspread.service_account(filename="creds/Formy-d40ed4e1b493.json")

if SPREADSHEET_URL:
    sh = gc.open_by_url("")
else:
    # note this is created on the service account so remember to share it with the owner
    if OWNER_EMAIL:
        sh = gc.create("A new spreadsheet")
        sh.share(OWNER_EMAIL, perm_type="user", role="writer")
    else:
        print("[X] KILLING BECAUSE YOU NEED AN EMAIL")
# if the cell doens't have a value then it fails
# print(sh.sheet1.get("A1"))
worksheet = sh.sheet1
worksheet.update_cell(1, 2, "Bingo!")
