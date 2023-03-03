import subprocess
import os

domain = input("Enter the domain name: ")
output_dir = domain + "_output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Assetfinder
print("[+] Running Assetfinder...")
assetfinder_output_file = os.path.join(output_dir, "assetfinder.txt")
assetfinder_cmd = f"assetfinder --subs-only {domain} > {assetfinder_output_file}"
subprocess.run(assetfinder_cmd, shell=True, check=True)

# Subfinder
print("[+] Running Subfinder...")
subfinder_output_file = os.path.join(output_dir, "subfinder.txt")
subfinder_cmd = f"subfinder -d {domain} -o {subfinder_output_file}"
subprocess.run(subfinder_cmd, shell=True, check=True)

# Amass
# print("[+] Running Amass...")
# amass_output_file = os.path.join(output_dir, "amass.txt")
# amass_cmd = f"amass enum -d {domain} -o {amass_output_file}"
# subprocess.run(amass_cmd, shell=True, check=True)

# Httpx
print("[+] Running Httpx...")
all_subdomains_file = os.path.join(output_dir, "all_subdomains.txt")
httpx_output_file = os.path.join(output_dir, "httpx.txt")
httpx_cmd = f"httpx -l {all_subdomains_file} -o {httpx_output_file} -title -status-code"
subprocess.run(httpx_cmd, shell=True, check=True)

# Dirsearch
print("[+] Running Dirsearch...")
dirsearch_output_file = os.path.join(output_dir, "dirsearch.txt")
dirsearch_cmd = f"dirsearch -u https://{domain} -e php,asp,aspx,jsp,html,txt,conf,config,bak,backup,swp -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -r -f -x 301,302,400,401,403,404,405,500,501,502,503,504,505 -o {dirsearch_output_file}"
subprocess.run(dirsearch_cmd, shell=True, check=True)

# Nikto
print("[+] Running Nikto...")
nikto_output_file = os.path.join(output_dir, "nikto.txt")
nikto_cmd = f"nikto -h {domain} -output {nikto_output_file}"
subprocess.run(nikto_cmd, shell=True, check=True)

# Wafw00f
print("[+] Running Wafw00f...")
wafw00f_output_file = os.path.join(output_dir, "wafw00f.txt")
wafw00f_cmd = f"wafw00f {domain} > {wafw00f_output_file}"
subprocess.run(wafw00f_cmd, shell=True, check=True)

# Waybackurls
print("[+] Running Waybackurls...")
waybackurls_output_file = os.path.join(output_dir, "waybackurls.txt")
waybackurls_cmd = f"waybackurls {domain} > {waybackurls_output_file}"
subprocess.run(waybackurls_cmd, shell=True, check=True)

# GitHound
print("[+] Running GitHound...")
githound_output_file = os.path.join(output_dir, "githound.txt")
githound_cmd = f"githound search {domain} > {githound_output_file}"
subprocess.run(githound_cmd, shell=True, check=True)

# GitRob
print("[+] Running GitRob...")
gitrob_output_dir = os.path.join(output_dir, "gitrob_output")
if not os.path.exists(gitrob_output_dir):
    os.makedirs(gitrob_output_dir)
gitrob_cmd = f"gitrob -o {gitrob_output_dir} -b -r -s {domain}"
subprocess.run(gitrob_cmd, shell=True, check=True)

# GitGraber
print("[+] Running GitGraber...")
gitgraber_output_file = os.path.join(output_dir, "gitgraber.txt")
gitgraber_cmd = f"gitgraber -q -s {domain} -o {gitgraber_output_file}"
subprocess.run(gitgraber_cmd, shell=True, check=True)
