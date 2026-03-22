import json
import os
import datetime
from packaging import version

def generate_index():
    extensions_dir = 'extensions'
    
    # Generate dynamic UTC ISO timestamp
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
    
    index_data = {
        "generatedAt": now_utc,
        "extensions": []
    }

    if not os.path.exists(extensions_dir):
        print("Extensions directory not found.")
        return

    # Replace YOUR_ORG/YOUR_REPO with values of your repository
    repo_url = "https://github.com/YOUR_ORG/YOUR_REPO"

    for extension_id in os.listdir(extensions_dir):
        extension_path = os.path.join(extensions_dir, extension_id)
        if not os.path.isdir(extension_path):
            continue

        versions = []
        # Find all version folders
        for v_dir in os.listdir(extension_path):
            v_path = os.path.join(extension_path, v_dir)
            metadata_file = os.path.join(v_path, 'metadata.json')
            
            if os.path.isdir(v_path) and os.path.exists(metadata_file):
                try:
                    with open(metadata_file, 'r') as f:
                        meta = json.load(f)
                        versions.append(meta)
                except Exception as e:
                    print(f"Error reading {metadata_file}: {e}")

        # Filter out metadata without a version key to avoid KeyError
        valid_versions = [v for v in versions if isinstance(v, dict) and 'version' in v]

        if valid_versions:
            # Sort versions using packaging.version to get the latest release
            valid_versions.sort(key=lambda x: version.parse(x['version']), reverse=True)
            
            # Add the latest version to the index
            latest = valid_versions[0]
            
            # Optional: Add link to the human-readable description
            info_md = os.path.join(extension_path, 'info.md')
            if os.path.exists(info_md):
                latest['infoUrl'] = f"{repo_url}/blob/main/{extension_path}/info.md"

            # Optional: Add link to the changelog
            changelog_md = os.path.join(extension_path, 'CHANGELOG.md')
            if os.path.exists(changelog_md):
                latest['changeLogUrl'] = f"{repo_url}/blob/main/{extension_path}/CHANGELOG.md"

            # Optional: Add links to assets
            assets_dir = os.path.join(extension_path, 'assets')
            if os.path.exists(assets_dir) and os.path.isdir(assets_dir):
                latest['assets'] = []
                for asset_file in os.listdir(assets_dir):
                    asset_path = os.path.join(assets_dir, asset_file)
                    if os.path.isfile(asset_path):
                        latest['assets'].append({
                            "name": asset_file,
                            "url": f"{repo_url}/blob/main/{asset_path}"
                        })

            index_data['extensions'].append(latest)

    with open('index.json', 'w') as f:
        json.dump(index_data, f, indent=2)
    print("Successfully generated index.json")

if __name__ == "__main__":
    generate_index()
