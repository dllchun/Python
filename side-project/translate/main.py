import polib
import pandas as pd
from googletrans import Translator


def po_to_excel():
    translator = Translator()
    po = polib.pofile("side-project/translate/zh-hant.po")

    data = []
    for entry in po:
        data.append([entry.msgctxt, entry.msgid, entry.msgstr, entry.comment])

    df = pd.DataFrame(data, columns=["msgctxt", "msgid", "msgstr", "comment"])

    df["tran_str"] = df["msgstr"].apply(
        lambda x: translator.translate(x, src="auto", dest="zh-TW")
    )

    df.to_excel("ro.xlsx", index=False)


# def excel_to_po():
#     df = pd.read_excel("ro-updated.xlsx")
#     df = df.astype(str)

#     po = polib.POFile()
#     for _, row in df.iterrows():
#         entry = polib.POEntry(
#             msgid=row["Message id"],
#             msgstr=row["zh-hant"],
#         )
#         po.append(entry)

#     po.save("zh-hant-1.po")


if __name__ == "__main__":
    po_to_excel()
