import subprocess

# Download the sense2vec model
subprocess.run(["wget", "https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz"])

# Extract the model
subprocess.run(["tar", "-xvf", "s2v_reddit_2015_md.tar.gz"])
