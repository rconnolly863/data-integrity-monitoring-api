# Data Integrity Monitoring API

A FastAPI-based backend service that compares structured datasets and detects discrepancies such as mismatched values and missing records.

## Overview

This project simulates a real-world data validation system where multiple data sources need to be reconciled. The API reads data from two sources, identifies inconsistencies, and exposes results through REST endpoints.

## Features

- Detects value mismatches between datasets
- Detects missing records across sources
- Provides a summary of detected issues
- Exposes functionality through a REST API
- Includes automated tests using pytest

## Tech Stack

- Python
- FastAPI
- pandas
- pytest

## Project Structure

