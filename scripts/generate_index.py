import json
import os
from packaging import version

def generate_index():
    modules_dir = 'modules'
    index_data = {
        "generatedAt": "2026-03-11T00:00:00Z", # You can use datetime.now().isoformat()
        "modules": []
    }

    if not os.path.exists(modules_dir):
        print("Modules directory not found.")
        return

    for module_id in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_id)
        if not os.path.isdir(module_path):
            continue

        versions = []
        # Find all version folders
        for v_dir in os.listdir(module_path):
            v_path = os.path.join(module_path, v_dir)
            metadata_file = os.path.join(v_path, 'metadata.json')
            
            if os.path.isdir(v_path) and os.path.exists(metadata_file):
                try:
                    with open(metadata_file, 'r') as f:
                        meta = json.load(f)
                        versions.append(meta)
                except Exception as e:
                    print(f"Error reading {metadata_file}: {e}")

        if versions:
            # Sort versions using packaging.version to get the latest release
            # Requires: pip install packaging
            versions.sort(key=lambda x: version.parse(x['version']), reverse=True)
            
            # Add the latest version to the index
            latest = versions[0]
            
            # Optional: Add link to the human-readable description
            info_md = os.path.join(module_path, 'info.md')
            if os.path.exists(info_md):
                latest['infoUrl'] = f"https://github.com/YOUR_ORG/YOUR_REPO/blob/main/modules/{module_id}/info.md"

            index_data['modules'].append(latest)

    with open('index.json', 'w') as f:
        json.dump(index_data, f, indent=2)
    print("Successfully generated index.json")

if __name__ == "__main__":
    generate_index()