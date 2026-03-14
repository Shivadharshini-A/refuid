# RefuID – Refugee Digital Identity System

RefuID is a prototype system designed to help border authorities manage refugees who arrive without official documents.  
The system creates a **temporary digital identity using biometric data** and allows officers to verify identities using **QR-based verification**.

---

## Problem

Millions of refugees arrive at borders without identification due to war, displacement, or disasters.  
This makes it difficult for authorities to:

- Verify identities
- Prevent duplicate registrations
- Track refugee status across checkpoints

RefuID provides a **digital identity solution for undocumented refugees**.

---

## Solution

RefuID captures biometric data and generates a **Digital Border ID** for each refugee.

The system:

1. Captures **facial image using webcam**
2. Records a **voice sample**
3. Generates a **unique digital identity**
4. Assigns a **temporary validity period**
5. Produces a **QR code for identity verification**
6. Allows officers to **search and verify identities**

---

## Features

- Face capture using webcam
- Voice recording
- Digital refugee identity generation
- Risk level classification
- QR code verification system
- Border officer search dashboard
- Temporary identity validity (3 months)

---

## Tech Stack

### Frontend
- React.js
- HTML
- CSS
- Web Camera API

### Backend
- Python
- FastAPI

### Identity System
- QR Code Verification
- Temporary in-memory storage (prototype)

---

---

## Demo Workflow

1. Border officer captures refugee **face image**
2. Officer records a **voice sample**
3. System generates **Digital Border ID**
4. Risk level is assigned
5. QR code is generated
6. Officers can scan the QR to verify identity instantly

---

## Future Improvements

- PostgreSQL database integration
- Advanced biometric matching
- Emotion and stress detection from voice
- Multi-checkpoint identity synchronization
- Secure biometric encryption

---

## Project Purpose

This project demonstrates how **biometric technology and digital identity systems** can support humanitarian efforts by helping authorities manage refugee identification safely and efficiently.

---

## Author

Dharshini A  
Hackathon Project – RefuID

## System Architecture
