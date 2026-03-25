# iDempiere Curated Extension Repository
This repository is a central, community-driven collection of extensions for **iDempiere ERP**. Each extension included here has been reviewed for compatibility and standard adherence.

## 🚀 How to Use

### 1. Browse the Extensions
You can explore extensions in two ways:
* **Manual Browsing:** Navigate the `extensions/` folder to see the list of available extension. Each folder contains an `info.md` with detailed documentation.
* **Machine Readable Index:** For developers or automated installers, a full catalog is available in index.json

### 2. Installation
To install an extension from this repository:
1. Use the Extension Management form in iDempiere Web Client to locate the extension and the specific version compatible with your iDempiere instance.
2. Click the install button in Extension Management form  to install the selected extension.
---
## 🛠 Repository Structure
The repository is organized to support multiple versions of the same extension:
```text
extensions/
└── <extension.symbolic.name>/
    ├── info.md             # Documentation and Screenshots
    ├── CHANGELOG.md        # Change log
    ├── assets/             # Static assets
    └── <version>/          # e.g., 1.0.0
        └── metadata.json   # Links to JARs and dependencies
```
---

## 🤝 How to Contribute
We welcome new extension! To submit yours:
1. **Fork** this repository.
2. Create a new folder under `extension/` following the naming convention.
3. Include `info.md` and the `metadata.json` with direct links to your release JARs (e.g., GitHub Releases).
4. Submit a **Pull Request**. Our automated CI will validate your JSON structure.

> [!IMPORTANT]
> Please ensure your extension follows iDempiere best practices (OSGi compliance, no hardcoding, proper licensing).
---
## 🤖 For Tool Developers

If you are building an extension manager for iDempiere, you can point your client to:
`https://raw.githubusercontent.com/<YOUR_ORG>/<YOUR_REPO>/main/index.json`
This file is automatically updated every time a new extension is merged.

## Create new repository from this template
1. Click the **Use this template** drop down menu, select **Create a new repository**
2. Edit README.md and scripts/generate_index.py
   - Replace **<YOUR_ORG>/<YOUR_REPO>** with values of your repository
