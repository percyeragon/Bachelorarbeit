import pandas as pd
from scipy import integrate
import numpy as np
def roundeffort(x):
    return 10*round(int(x)/10)
StandardNormal = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Normal/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardNormal['approach'] = 'HiCal'
StandardReferenzen = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Referenzen/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardReferenzen['approach'] = 'HiCal mit DeepCT(Referenzen)'
StandardReferenzenStemStop = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/ReferenzenStemStop/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardReferenzenStemStop['approach'] = 'HiCal mit DeepCT(ReferenzenStemStop)'
StandardTitel = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Titel/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardTitel['approach'] = 'HiCal mit DeepCT(Titel)'
StandardTitelStemStop = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/TitelStemStop/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardTitelStemStop['approach'] = 'HiCal mit DeepCT(TitelStemStop)'
StandardZitate = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Zitate/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardZitate['approach'] = 'HiCal mit DeepCT(Zitate)'
StandardZitateStemStop = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/ZitateStemStop/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
StandardZitateStemStop['approach'] = 'HiCal mit DeepCT(ZitateStemStop)'
VolltextNormal = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/Normal/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextNormal['approach'] = 'HiCal Volltext'
VolltextReferenzen = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/Referenzen/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextReferenzen['approach'] = 'HiCal Volltext mit DeepCT(Referenzen)'
VolltextReferenzenStemStop = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/ReferenzenStemStop/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextReferenzenStemStop['approach'] = 'HiCal Volltext mit DeepCT(ReferenzenStemStop)'
VolltextTitel = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/Titel/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextTitel['approach'] = 'HiCal Volltext mit DeepCT(Titel)'
VolltextTitelStemStop = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/TitelStemStop/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextTitelStemStop['approach'] = 'HiCal Volltext mit DeepCT(TitelStemStop)'
VolltextZitate = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/Zitate/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextZitate['approach'] = 'HiCal Volltext mit DeepCT(Zitate)'
VolltextZitateStemStop = pd.read_csv('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/ZitateStemStop/output/bmi_42.avg.precisionrecall', delimiter=r"\s+")
VolltextZitateStemStop['approach'] = 'HiCal Volltext mit DeepCT(ZitateStemStop)'

df = pd.concat([StandardNormal])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardNormal",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([StandardReferenzen])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardReferenzen",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([StandardReferenzenStemStop])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardReferenzenStemStop",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([StandardTitel])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardTitel",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([StandardTitelStemStop])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardTitelStemStop",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([StandardZitate])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardZitate",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([StandardZitateStemStop])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("StandardZitateStemStop",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))

df = pd.concat([VolltextNormal])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextNormal",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([VolltextReferenzen])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextReferenzen",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([VolltextReferenzenStemStop])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextReferenzenStemStop",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([VolltextTitel])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextTitel",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([VolltextTitelStemStop])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextTitelStemStop",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([VolltextZitate])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextZitate",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))
df = pd.concat([VolltextZitateStemStop])
df['effort_rounded'] = df.effort.apply(lambda i: roundeffort(i))
print("VolltextZitateStemStop",np.trapz(integrate.cumtrapz(df['effort_rounded'], df['recall'], initial=0)))