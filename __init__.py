import numpy as np
import pandas as pd
import os


z = [75020, 75021, 75058, 75076, 75090, 75092, 75414, 75415, 75418, 75424, 75428]


def path1():
    csv_path = os.path.join(r"2003_master_data.csv")
    df = pd.read_csv(csv_path)
    return df


def path2():
    csv_path = os.path.join(r"C:\Users\E6420\Desktop\2017master2.csv")
    df2 = pd.read_csv(csv_path)
    return df2


def zip_code(df):
    a = df.loc[df["PZIP2"].isin(z)]

    return a


def total(a):
    b = a.loc[:, ["SPEC1"]]
    c = b.count()
    d = np.sum(c)
    return d


def family(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'FAMILY MEDICINE') | (b["SPEC1"] == "FAMILY PRACTICE") | (b["SPEC1"] == 'GENERAL PRACTICE')
         | (b["SPEC1"] == "GENERAL PREVENTIVE MEDICINE"))
    d = np.sum(c)

    return d


def ob(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'OBSTETRICS') | (b["SPEC1"] == "OBSTETRICS AND GYNECOLOGY"))
    d = np.sum(c)

    return d


def pediatrics(a):
    b = a.loc[:, ["SPEC1"]]
    c = (b["SPEC1"] == 'PEDIATRICS')
    d = np.sum(c)

    return d


def vascular(a):
    b = a.loc[:, ["SPEC1"]]
    c = (b["SPEC1"] == 'VASCULAR SURGERY')
    d = np.sum(c)

    return d


def intmed(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'INTERNAL MEDICINE') | (b["SPEC1"] == "GERIATRICS") |
         (b["SPEC1"] == 'GERIATRICS ‐ INTERNAL MEDICINE') | (b["SPEC1"] == "GERIATRICS GENERAL PRACTICE"))
    d = np.sum(c)

    return d


def emergency(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'EMERGENCY MEDICAL SERVICES') | (b["SPEC1"] == "EMERGENCY MEDICINE") |
         (b["SPEC1"] == 'FAMILY PRACTICE ‐ EMERGENCY MED') | (b["SPEC1"] == "INTERNAL MED ‐ EMERGENCY MED"))
    d = np.sum(c)

    return d


def neurosurgeons(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'CRITICAL CARE ‐ NEUROSURGERY') | (b["SPEC1"] == "NEUROLOGICAL SURGERY "))
    d = np.sum(c)

    return d

def anest(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'ANESTHESIOLOGY') | (b["SPEC1"] == "ANESTHESIOLOGY ‐ PAIN MANAGEMENT") |
         (b["SPEC1"] == 'CARDIOTHORACIC ANESTHESIOLOGY') | (b["SPEC1"] == "CRITICAL CARE ANESTHESIOLOGY")
         | (b["SPEC1"] == "PEDIATRIC ANESTHESIOLOGY (PEDS)"))
    d = np.sum(c)

    return d


def ortho(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'HAND SURGERY ‐ ORTHOPEDIC SURGERY') | (b["SPEC1"] == "ORTHOPEDIC SURGERY") |
         (b["SPEC1"] == 'ORTHOPEDIC SURGERY OF THE SPINE'))
    d = np.sum(c)

    return d


def cardiologist(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'CARDIOLOGY') | (b["SPEC1"] == "CARDIOVASCULAR DISEASES"))
    d = np.sum(c)

    return d


def cardiothoracic(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'CARDIOVASCULAR SURGERY') | (b["SPEC1"] == "PEDIATRIC CARDIOTHORACIC SURGERY") |
         (b["SPEC1"] == 'THORACIC CARDIOVASCULAR SURGERY') | (b["SPEC1"] == "THORACIC SURGERY"))
    d = np.sum(c)

    return d

def pediatricsub(a):
    b = a.loc[:, ["SPEC1"]]
    c = ((b["SPEC1"] == 'PEDIATRIC ANESTHESIOLOGY (PEDS)') | (b["SPEC1"] == "PEDIATRIC CARDIOTHORACIC SURGERY") |
         (b["SPEC1"] == 'PEDIATRIC CRITICAL CARE MEDICINE') | (b["SPEC1"] == "PEDIATRIC DERMATOLOGY") |
         (b["SPEC1"] == 'PEDIATRIC EMERGENCY MEDICINE (EM)') | (b["SPEC1"] == "PEDIATRIC EMERGENCY MEDICINE (PEDS)") |
         (b["SPEC1"] == 'PEDIATRIC ENDOCRINOLOGY') | (b["SPEC1"] == "PEDIATRIC FORENSIC MEDICINE") |
         (b["SPEC1"] == 'PEDIATRIC GASTROENTEROLOGY') | (b["SPEC1"] == "PEDIATRIC HEMATOLOGY/ONCOLOGY") |
         (b["SPEC1"] == 'PEDIATRIC INFECTIOUS DISEASE') | (b["SPEC1"] == "PEDIATRIC INTENSIVE CARE") |
         (b["SPEC1"] == 'PEDIATRIC NEPHROLOGY') | (b["SPEC1"] == "PEDIATRIC NEUROLOGY") |
         (b["SPEC1"] == 'PEDIATRIC OPHTHALMOLOGY') | (b["SPEC1"] == "PEDIATRIC ORTHOPEDICS") |
         (b["SPEC1"] == 'PEDIATRIC OTOLARYNGOLOGY') | (b["SPEC1"] == "PEDIATRIC PATHOLOGY") |
         (b["SPEC1"] == 'PEDIATRIC PSYCHIATRY') | (b["SPEC1"] == "PEDIATRIC PULMONOLOGY") |
         (b["SPEC1"] == 'PEDIATRIC RADIOLOGY') | (b["SPEC1"] == "PEDIATRIC REHABILITATION MEDICINE") |
         (b["SPEC1"] == 'PEDIATRIC RHEUMATOLOGY') | (b["SPEC1"] == "PEDIATRIC SURGERY ") |
         (b["SPEC1"] == 'PEDIATRIC SURGERY (NEUROLOGY)') | (b["SPEC1"] == "PEDIATRIC UROLOGY") |
         (b["SPEC1"] == 'PEDIATRICS, ALLERGY') | (b["SPEC1"] == "PEDIATRICS, ALLERGY & IMMUNOLOGY") |
         (b["SPEC1"] == 'PEDIATRICS, CARDIOLOGY') | (b["SPEC1"] == "PEDIATRICS, MEDICAL GENETICS") )
    d = np.sum(c)

    return d


def compute_percentage(yr1, yr2):
    pct = float(yr2/yr1.sum()-1) * 100
    return round(pct, 2)


ob1 = ob(zip_code(path1()))
ped1 = pediatrics(zip_code(path1()))
fam1 = family(zip_code(path1()))
intmed1 = intmed(zip_code(path1()))
pedsub1 = pediatricsub(zip_code(path1()))
vassur1 = vascular(zip_code(path1()))
emer1 = emergency(zip_code(path1()))
neuro1 = neurosurgeons(zip_code(path1()))
anest1 = anest(zip_code(path1()))
ortho1 = ortho(zip_code(path1()))
cardio1 = cardiologist(zip_code(path1()))
cardiothor1 = cardiothoracic(zip_code(path1()))
pedsub2 = pediatricsub(zip_code(path2()))
vassur2 = vascular(zip_code(path2()))
emer2 = emergency(zip_code(path2()))
neuro2 = neurosurgeons(zip_code(path2()))
anest2 = anest(zip_code(path2()))
ortho2 = ortho(zip_code(path2()))
cardio2 = cardiologist(zip_code(path2()))
cardiothor2 = cardiothoracic(zip_code(path2()))
fam2 = family(zip_code(path2()))
ob2 = ob(zip_code(path2()))
ped2 = pediatrics(zip_code(path2()))
intmed2 = intmed(zip_code(path2()))
total1 = total(zip_code(path1()))
total2 = total(zip_code(path2()))

fampct2 = compute_percentage(fam1, fam2)
obpct2 = compute_percentage(ob1, ob2)
intmedpct2 = compute_percentage(intmed1, intmed2)
pedpct2 = compute_percentage(ped1, ped2)
pedsubpct2 = compute_percentage(pedsub1, pedsub2)
vassurpct2 = compute_percentage(vassur1, vassur2)
emerpct2 = compute_percentage(emer1, emer2)
neuropct2 = compute_percentage(neuro1, neuro2)
anestpct2 = compute_percentage(anest1, anest2)
orthopct2 = compute_percentage(ortho1, ortho2)
caeriopct2 = compute_percentage(cardio1, cardio2)
cardiothorpct2 = compute_percentage(cardiothor1, cardiothor2)


f = pd.Series({"2003": fam1, "2017": fam2, "difference": fam2 - fam1, "Pct Change": fampct2})
f1 = pd.Series({"2003": intmed1, "2017": intmed2, "difference": intmed2 - intmed1, "Pct Change": intmedpct2})
f2 = pd.Series({"2003": ob1, "2017": ob2, "difference": ob2 - ob1, "Pct Change": obpct2})
f3 = pd.Series({"2003": ped1, "2017": ped2, "difference": ped2 - ped1, "Pct Change": pedpct2})
l = pd.DataFrame([f, f1, f2, f3], index=["Family Practice and General Practice", "Internal Medicine and Geriatrics", "OB/GYN", "Pediatrics"])
print(l)

o = pd.Series({"2003": pedsub1, "2017": pedsub2, "difference": pedsub2 - pedsub1, "Pct Change": pedsubpct2})
o1 = pd.Series({"2003": vassur1, "2017": vassur2, "difference": vassur2 - vassur1, "Pct Change": vassurpct2})
o2 = pd.Series({"2003": emer1, "2017": emer2, "difference": emer2 - emer1, "Pct Change": emerpct2})
o3 = pd.Series({"2003": neuro1, "2017": neuro2, "difference": neuro2 - neuro1, "Pct Change": neuropct2})
o4 = pd.Series({"2003": anest1, "2017": anest2, "difference": anest2 - anest1, "Pct Change": anestpct2})
o5 = pd.Series({"2003": ortho1, "2017": ortho2, "difference": ortho2 - ortho1, "Pct Change": orthopct2})
o6 = pd.Series({"2003": ob1, "2017": ob2, "difference": ob2 - ob1, "Pct Change": obpct2})
o7 = pd.Series({"2003": cardio1, "2017": cardio2, "difference": cardio2 - cardio1, "Pct Change": caeriopct2})
o8 = pd.Series({"2003": cardiothor1, "2017": cardiothor2, "difference": cardiothor2 - cardiothor1, "Pct Change": cardiothorpct2})
p = pd.DataFrame([o, o1, o2, o3, o4, o5, o6, o7, o8], index=["Pediatric sub-specialists", "Vascular Surgeons", "Emergency Care Doctors"
, "Neurosurgeons", "Anesthesiologists", "Orthopedic Surgeons", "Ob/Gyn", "Cardiologists", "Cardiovascular and Thoracic Surgeons"])
print(p)

tot = pd.Series({"2003": total1, "2017": total2, "difference": total2 - total1})
tot2 = pd.DataFrame([tot], index = ["District Totals"])
writer = pd.ExcelWriter(r"C:\Users\E6420\Desktop\HD127.xlsx")
H = l.copy()
H.to_excel(writer, sheet_name="Primary Care", index=True)
G = p.copy()
G.to_excel(writer, sheet_name="High Risk", index=True)
I = tot2.copy()
I.to_excel(writer, sheet_name="Total Physicians", index=True)
writer.save()

