import amino
from io import BytesIO
from requests import get
print("""\u001b[31m
Script by deluvsushi
Github : https://github.com/deluvsushi
╭━━━╮╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╭━╮╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱┃╭╯┃┃
┃┃╱┃┣╮╭┳┳━╮╭━━┫┃╱╰╋━━┳━━┳╮╱╭┫╰━╯┣━┳━━┳╯╰┳┫┃╭━━╮
┃╰━╯┃╰╯┣┫╭╮┫╭╮┃┃╱╭┫╭╮┃╭╮┃┃╱┃┃╭━━┫╭┫╭╮┣╮╭╋┫┃┃┃━┫
┃╭━╮┃┃┃┃┃┃┃┃╰╯┃╰━╯┃╰╯┃╰╯┃╰━╯┃┃╱╱┃┃┃╰╯┃┃┃┃┃╰┫┃━┫
╰╯╱╰┻┻┻┻┻╯╰┻━━┻━━━┻━━┫╭━┻━╮╭┻╯╱╱╰╯╰━━╯╰╯╰┻━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╰━━╯
""")
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_code(
    input("-- User link::: ")).json["extensions"]["linkInfo"]
com_id, user_id = link_info["ndcId"], link_info["objectId"]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
user_info = sub_client.get_user_info(userId=user_id).json
nickname = user_info["nickname"]
description = user_info["content"]
icon = BytesIO(get(user_info["icon"]).content)
profile_style = user_info["extensions"]["style"]
image_list = [BytesIO(get(str(user_info["mediaList"]).split("'")[1]).content)]
if "backgroundColor" in profile_style:
    background_color = profile_style["backgroundColor"]
    sub_client.edit_profile(backgroundColor=background_color)
elif "backgroundMediaList" in profile_style:
    background_image = str(profile_style["backgroundMediaList"]).split("'")[1]
    sub_client.edit_profile(backgroundImage=background_image)

sub_client.edit_profile(
    nickname=nickname,
    content=description,
    icon=icon,
    imageList=image_list)
print("-- Successfully copied profile!")
