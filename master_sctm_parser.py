import sys

with open(sys.argv[1], 'r') as f:
    master_sctm = f.read()
f.closed()

for line in master_sctm:
    (nist_ref_num, control_family, org_ref_num,
     baseline_low, baseline_moderate, baseline_high,
     confidentiality_low, confidentiality_moderate,
     confidentiality_high, integrity_low, integrity_moderate,
     integrity_high, availability_low, availability_moderate,
     availability_high, references, redhat_response,
     requirements, suppemental_guidance) = line.split(',')
