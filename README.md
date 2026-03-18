# iDempiere Curated Module Repository
This repository is a central, community-driven collection of modules for **iDempiere ERP**. Each module included here has been reviewed for compatibility and standard adherence.

## 🚀 How to Use

### 1. Browse the Modules
You can explore modules  in two ways:
* **Manual Browsing:** Navigate the `modules/` folder to see the list of available module. Each folder contains an `info.md` with detailed documentation.
* **Machine Readable Index:** For developers or automated installers, a full catalog is available in index.json

### 2. Installation
To install a module from this repository:
1.  Use the Module Management form in iDempiere Web Client to locate the module and the specific version compatible with your iDempiere instance.
2. Click the install button in Module Management form  to install the selected module.
---
## 🛠 Repository Structure
The repository is organized to support multiple versions of the same module:
```text
modules/
└── <module.symbolic.name>/
    ├── info.md             # Documentation and Screenshots
    └── <version>/          # e.g., 1.0.0
        └── metadata.json   # Links to JARs and dependencies
```
---

## 🤝 How to Contribute
We welcome new modules! To submit yours:
1. **Fork** this repository.
2. Create a new folder under `module/` following the naming convention.
3. Include `info.md` and the `metadata.json` with direct links to your release JARs (e.g., GitHub Releases).
4. Submit a **Pull Request**. Our automated CI will validate your JSON structure.

> [!IMPORTANT]
> Please ensure your module follows iDempiere best practices (OSGi compliance, no hardcoding, proper licensing).
---
## 🤖 For Tool Developers

If you are building a module manager for iDempiere, you can point your client to:
`https://raw.githubusercontent.com/<YOUR_ORG>/<YOUR_REPO>/main/index.json`
This file is automatically updated every time a new module is merged.

