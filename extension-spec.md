# iDempiere Extension

## Folder Structure

```Text
com.example.plugin.name/   
├── info.md
└── assets/
└── 1.0.0/
    ├── core-logic-1.0.0.jar
    └── metadata.json
```
- Root is extension name
- info.md: Human-readable description
- assets: Static assets (image, csv, etc)
- 1.0.0: Version-specific folder
- metadata.json: Technical metadata & bundle links

## Extension Info

### info. md
- Should have the following sections:
  - Summary
  - Features
  - Compatibility
  - Database Changes (if any)
  - Usage & Configuration
  - Author/Support

### Example Info.md

```md
# Enhanced PDF Reporting

**Summary:** Replaces the standard iDempiere PDF engine with a layout-aware generator supporting custom headers, watermarks, and QR codes.

## 🚀 Features

* **Custom Watermarking:** Add "Draft" or "Confidential" watermarks based on document status.
* **QR Code Integration:** Automatically injects a QR code for document verification.
* **Optimized Compression:** Reduces file size for large batch reports by up to 40%.
* **Font Embedding:** Full support for custom TTF fonts to match corporate branding.

## ⚙️ Compatibility

* **iDempiere Version:** 11.0, 12.0
* **Java Version:** 17+
* **Database:** PostgreSQL (Optimized), Oracle (Compatible)

## 📦 Database Changes

* **System PackIn:** This extension will install a system tenant `PackIn` for new Window and Field configurations.
* **Tenant PackIn:** Download from {url of 2pack} and install into the destination tenant
* **Tenant CSV Import:** Download from {url of csv file} and install into the destination tenant

## 🛠 Usage & Configuration

After installation, navigate to **System Admin > Tenant > Report PDF Configuration**.

* Set the **Watermark Text** field to use dynamic context variables (e.g., `@DocumentNo@`).
* To enable QR codes, ensure the report query includes the `DocumentUUID` column.

## 📸 Screenshots

*Figure 1: The new configuration UI for defining report watermarks.*

## 👤 Author / Support

* **Developer:** [Your Name/Org]
* **Source Code:** [Link to GitHub/GitLab]
* **Issue Tracker:** [Link to Issues]

```

## Metadata

### Json Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "iDempiere Extension Metadata",
  "type": "object",
  "required": ["id", "version", "idempiereVersion", "bundles", "entityType"],
  "properties": {
    "id": {
      "type": "string",
      "description": "The unique identifier for the extension (usually the symbolic name)."
    },
    "version": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+(-[a-zA-Z0-9]+)?$",
      "description": "Semantic versioning string (e.g., 1.0.0)."
    },
    "idempiereVersion": {
      "type": "string",
      "description": "The major version of iDempiere supported (e.g., '11' or '12')."
    },
    "releaseDate": {
      "type": "string",
      "format": "date",
      "description": "The date of the release in YYYY-MM-DD format."
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "categories": {
      "type": "array",
      "items": { "type": "string" },
      "uniqueItems": true
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "uniqueItems": true
    },
    "entityType": {
      "type": "string",
      "description": "Identifies the type of entity, often matching the ID or a specific extension class."
    },
    "bundles": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["symbolicName", "downloadUrl"],
        "properties": {
          "symbolicName": { "type": "string" },
          "downloadUrl": { "type": "string", "format": "uri" },
          "sha256": { "type": "string" }
        }
      }
    },
    "dependencies": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "version"],
        "properties": {
          "id": { "type": "string" },
          "version": { "type": "string" }
        }
      }
    }
  }
}

```

### Example metadata
```
{
  "id": "com.example.extension.name",
  "version": "1.0.0",
  "idempiereVersion": "11",
  "releaseDate": "2026-03-11",
  "name": "Extension Name",
  "description": "Short description of this specific version.",
  "categories": [“category1”, “category2”],
  "tags": [“tag1”, “tag2”],
  "entityType": "com.example.extension.name"
  "bundles": [
    {
      "symbolicName": "com.example.plugin.core",
      "downloadUrl": "https://github.com/user/repo/releases/download/v1.0.0/com.example.plugin.core_1.0.0.jar",
      "sha256": "optional-hash-for-verification"
    },
    {
      "symbolicName": "com.example.plugin.ui",
      "downloadUrl": "https://github.com/user/repo/releases/download/v1.0.0/com.example.plugin.ui_1.0.0.jar"
    }
  ],
  "dependencies": [
    {
      "id": "org.idempiere.p2.feature",
      "version": "11.0.0"
    }
  ]
}
```
