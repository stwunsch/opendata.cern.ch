import json
import copy

path = "cernopendata/modules/fixtures/data/records/cms-derived-nanoaod-outreach-higgstautau.json"

d = json.load(open(path, "r"))
ref = d[0]
if ref["recid"] != "12351":
    raise Exception

links = [
        8001,
        9743,
        7730,
        9518,
        9863,
        9864,
        9865,
        6024,
        6050,
        ]
titles = [
    "GluGluToHToTauTau",
    "VBF_HToTauTau",
    "DYJetsToLL",
    "TTbar",
    "W1JetsToLNu",
    "W2JetsToLNu",
    "W3JetsToLNu",
    "Run2012B_TauPlusX",
    "Run2012C_TauPlusX"
        ]
events = [
        476963,
        491653,
        30458871,
        6423106,
        29784800,
        30693853,
        15241144,
        35647508,
        51303171
        ]
sizes = [
        196517149,
        231849713,
        9247252629,
        3528995041,
        10731401995,
        12161887620,
        6544850738,
        10918632568,
        15886107547
        ]
hashes = [
        "2b025925",
        "8967f330",
        "dfd0d57c",
        "99ffd168",
        "e5d19fd7",
        "26b03d60",
        "5a2b198a",
        "8b8629d5",
        "5590ee9f"
        ]

n = []
for i in range(len(titles)):
    tmp = copy.deepcopy(ref)
    tmp["validation"]["links"][0]["recid"] = str(links[i])
    tmp["recid"] = str(int(12351+i))
    tmp["title"] = ref["title"].replace("GluGluToHToTauTau", titles[i])
    tmp["files"][0]["uri"] = "root://eospublic.cern.ch//eos/opendata/cms/software/HiggsTauTauNanoAODOutreachAnalysis/" + titles[i] + ".root"
    tmp["files"][0]["checksum"] = "adler32:" + hashes[i]
    tmp["files"][0]["size"] = sizes[i]
    tmp["distribution"]["size"] = sizes[i]
    tmp["distribution"]["number_events"] = events[i]
    n.append(tmp)

json.dump(n, open(path, "w"), sort_keys=True, indent=4, separators=(',', ': '))
