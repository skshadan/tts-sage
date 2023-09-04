from huggingface_hub import hf_hub_download
import shutil  # Make sure to import this

# Download the model checkpoint
hf_hub_download(repo_id="youmebangbang/vits_tts_models", filename="joel_osteen_checkpoint_2550000.pth")

# Rename the file
shutil.move("/home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/joel_osteen_checkpoint_2550000.pth", "/home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/model_file.pth")

# Download the config.json file
hf_hub_download(repo_id="youmebangbang/vits_tts_models", filename="config.json")

