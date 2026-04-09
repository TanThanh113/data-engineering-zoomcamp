Terraform & GCP: Service Account Impersonation
This project demonstrates how to establish a secure "bridge" between Terraform and Google Cloud Platform (GCP) using Service Account Impersonation—a modern, secure alternative to static JSON keys.

🌟 Key Benefits
Enhanced Security: Eliminates the risk of leaking sensitive credential files.

Seamless Automation: Leverages Google's Application Default Credentials (ADC).

Centralized Control: Manages access directly through IAM roles and identities.

🛠 Workflow Overview
Initialization: Set up the GCP Project and Service Account via the Console.

Authentication: Sign in and configure ADC using the Google Cloud CLI.

Authorization: Grant the serviceAccountTokenCreator role to your user identity.

Deployment: Use Terraform's "Alias Provider" to borrow Service Account tokens for resource creation.

📖 Essential Commands
terraform init: Initialize the working directory.

terraform plan: Preview infrastructure changes.

terraform apply: Deploy and build the resources.

terraform destroy: Clean up and remove all resources to avoid costs.

This repository is intended for learning and implementing secure Infrastructure as Code (IaC) practices.
