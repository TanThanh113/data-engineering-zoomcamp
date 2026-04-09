# Terraform & GCP: Service Account Impersonation

This project demonstrates how to establish a secure "bridge" between **Terraform** and **Google Cloud Platform (GCP)** using **Service Account Impersonation**—a modern, secure alternative to static JSON keys.

---

## 🌟 Key Benefits

* **Enhanced Security**: Eliminates the risk of leaking sensitive credential files (JSON keys).
* **Seamless Automation**: Leverages Google's Application Default Credentials (ADC).
* **Centralized Control**: Manages access directly through IAM roles and identities.

## 🛠 Workflow Overview

1.  **Initialization**: Set up the GCP Project and Service Account via the Google Cloud Console.
2.  **Authentication**: Sign in and configure ADC using the Google Cloud CLI (`gcloud auth application-default login`).
3.  **Authorization**: Grant the `serviceAccountTokenCreator` role to your user identity for the specific Service Account.
4.  **Deployment**: Use Terraform's **Alias Provider** to borrow Service Account tokens for resource creation.

## 📖 Essential Commands

Use the following commands to manage your infrastructure:

```bash
# Initialize the working directory and download providers
terraform init

# Preview infrastructure changes before applying
terraform plan

# Deploy and build the resources (requires confirmation)
terraform apply

# Clean up and remove all resources to avoid costs
terraform destroy
