# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps['spring-cloud'] = """
    type: group
    short-summary: Commands to manage Azure Spring Cloud.
"""

helps['spring-cloud create'] = """
    type: command
    short-summary: Create an Azure Spring Cloud.
    examples:
    - name: Create a new Azure Spring Cloud in westus.
      text: az spring-cloud create -n MyService -g MyResourceGroup -l westus
    - name: Create a new Azure Spring Cloud in westus with an existing Application Insights by using the Connection string (recommended) or Instrumentation key.
      text: az spring-cloud create -n MyService -g MyResourceGroup -l westus --app-insights-key \"MyConnectionString\"
    - name: Create a new Azure Spring Cloud in westus with an existing Application Insights.
      text: az spring-cloud create -n MyService -g MyResourceGroup -l westus --app-insights appInsightsName
    - name: Create a new Azure Spring Cloud in westus with an existing Application Insights and specify the sampling rate.
      text: az spring-cloud create -n MyService -g MyResourceGroup -l westus --app-insights appInsightsName --sampling-rate 10
    - name: Create a new Azure Spring Cloud with Application Insights disabled.
      text: az spring-cloud create -n MyService -g MyResourceGroup --disable-app-insights
    - name: Create a new Azure Spring Cloud with VNet-injected via giving VNet name in current resource group
      text: az spring-cloud create -n MyService -g MyResourceGroup --vnet MyVNet --app-subnet MyAppSubnet --service-runtime-subnet MyServiceRuntimeSubnet
    - name: Create a new Azure Spring Cloud with VNet-injected via giving subnets resource ID
      text: az spring-cloud create -n MyService -g MyResourceGroup --app-subnet /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyVnetRg/providers/Microsoft.Network/VirtualNetworks/test-vnet/subnets/app --service-runtime-subnet /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyVnetRg/providers/Microsoft.Network/VirtualNetworks/test-vnet/subnets/svc --reserved-cidr-range 10.0.0.0/16,10.1.0.0/16,10.2.0.1/16
    - name: Create a Azure Spring Cloud Enterprise instance if the Azure Subscription never hosts Azure Spring Cloud Enterprise instance
      text: |
        az provider register -n Microsoft.SaaS
        az term accept --publisher vmware-inc --product azure-spring-cloud-vmware-tanzu-2 --plan tanzu-asc-ent-mtr
        az spring-cloud create -n MyService -g MyResourceGroup --sku Enterprise
"""

helps['spring-cloud update'] = """
    type: command
    short-summary: Update an Azure Spring Cloud.
    examples:
    - name: Update pricing tier.
      text: az spring-cloud update -n MyService --sku Standard -g MyResourceGroup
    - name: Update the tags of the existing Azure Spring Cloud.
      text: az spring-cloud update -n MyService -g MyResourceGroup --tags key1=value1 key2=value2
"""

helps['spring-cloud delete'] = """
    type: command
    short-summary: Delete an Azure Spring Cloud.
"""

helps['spring-cloud start'] = """
    type: command
    short-summary: Start an Azure Spring Cloud.
"""

helps['spring-cloud stop'] = """
    type: command
    short-summary: Stop an Azure Spring Cloud.
"""

helps['spring-cloud list'] = """
    type: command
    short-summary: List all Azure Spring Cloud in the given resource group, otherwise list the subscription's.
"""

helps['spring-cloud show'] = """
    type: command
    short-summary: Show the details for an Azure Spring Cloud.
"""

helps['spring-cloud test-endpoint'] = """
    type: group
    short-summary: Commands to manage test endpoint in Azure Spring Cloud.
"""

helps['spring-cloud test-endpoint enable'] = """
    type: command
    short-summary: Enable test endpoint of the Azure Spring Cloud.
"""

helps['spring-cloud test-endpoint disable'] = """
    type: command
    short-summary: Disable test endpoint of the Azure Spring Cloud.
"""

helps['spring-cloud test-endpoint list'] = """
    type: command
    short-summary: List test endpoint keys of the Azure Spring Cloud.
"""

helps['spring-cloud test-endpoint renew-key'] = """
    type: command
    short-summary: Regenerate a test-endpoint key for the Azure Spring Cloud.
"""

helps['spring-cloud storage'] = """
    type: group
    short-summary: Commands to manage Storages in Azure Spring Cloud.
"""

helps['spring-cloud storage add'] = """
    type: command
    short-summary: Create a new storage in the Azure Spring Cloud.
    examples:
    - name: Create a Storage resource with your own storage account.
      text: az spring-cloud storage add --storage-type StorageAccount --account-name MyAccountName --account-key MyAccountKey  -g MyResourceGroup -s MyService -n MyStorageName
"""

helps['spring-cloud storage update'] = """
    type: command
    short-summary: Update an existing storage in the Azure Spring Cloud.
    examples:
    - name: Update a Storage resource with new name or new key.
      text: az spring-cloud storage update --storage-type StorageAccount --account-name MyAccountName --account-key MyAccountKey  -g MyResourceGroup -s MyService -n MyStorageName
"""

helps['spring-cloud storage show'] = """
    type: command
    short-summary: Get an existing storage in the Azure Spring Cloud.
    examples:
    - name: Get a Storage resource.
      text: az spring-cloud storage show -g MyResourceGroup -s MyService -n MyStorageName
"""

helps['spring-cloud storage list'] = """
    type: command
    short-summary: List all existing storages in the Azure Spring Cloud.
    examples:
    - name: List all Storage resources.
      text: az spring-cloud storage list -g MyResourceGroup -s MyService
"""

helps['spring-cloud storage remove'] = """
    type: command
    short-summary: Remove an existing storage in the Azure Spring Cloud.
    examples:
    - name: Remove a Storage resource.
      text: az spring-cloud storage remove -g MyResourceGroup -s MyService -n MyStorageName
"""

helps['spring-cloud storage list-persistent-storage'] = """
    type: command
    short-summary: List all the persistent storages related to an existing storage in the Azure Spring Cloud.
    examples:
    - name: list all the persistent-storage related to an existing storage.
      text: az spring-cloud storage list-persistent-storage -g MyResourceGroup -s MyService -n MyStorageName
"""

helps['spring-cloud app'] = """
    type: group
    short-summary: Commands to manage apps in Azure Spring Cloud.
"""

helps['spring-cloud app create'] = """
    type: command
    short-summary: Create a new app with a default deployment in the Azure Spring Cloud.
    examples:
    - name: Create an app with the default configuration.
      text: az spring-cloud app create -n MyApp -s MyCluster -g MyResourceGroup
    - name: Create an public accessible app with 3 instances and 2 cpu cores and 3 GB of memory per instance.
      text: az spring-cloud app create -n MyApp -s MyCluster -g MyResourceGroup --assign-endpoint true --cpu 2 --memory 3 --instance-count 3
"""

helps['spring-cloud app append-persistent-storage'] = """
    type: command
    short-summary: Append a new persistent storage to an app in the Azure Spring Cloud.
    examples:
    - name: Append a new persistent storage to an app.
      text: az spring-cloud app append-persistent-storage --persistent-storage-type AzureFileVolume --share-name MyShareName --mount-path /MyMountPath --storage-name MyStorageName -n MyApp -g MyResourceGroup -s MyService
"""

helps['spring-cloud app update'] = """
    type: command
    short-summary: Update configurations of an app.
    examples:
    - name: Add an environment variable for the app.
      text: az spring-cloud app update -n MyApp -s MyCluster -g MyResourceGroup --env foo=bar
"""

helps['spring-cloud app delete'] = """
    type: command
    short-summary: Delete an app in the Azure Spring Cloud.
"""

helps['spring-cloud app list'] = """
    type: command
    short-summary: List all apps in the Azure Spring Cloud.
    examples:
    - name: Query status of persistent storage of all apps
      text: az spring-cloud app list -s MyCluster -g MyResourceGroup -o json --query '[].{Name:name, PersistentStorage:properties.persistentDisk}'
"""

helps['spring-cloud app show'] = """
    type: command
    short-summary: Show the details of an app in the Azure Spring Cloud.
"""

helps['spring-cloud app start'] = """
    type: command
    short-summary: Start instances of the app, default to production deployment.
"""

helps['spring-cloud app stop'] = """
    type: command
    short-summary: Stop instances of the app, default to production deployment.
"""

helps['spring-cloud app restart'] = """
    type: command
    short-summary: Restart instances of the app, default to production deployment.
"""

helps['spring-cloud app deploy'] = """
    type: command
    short-summary: Deploy source code or pre-built binary to an app and update related configurations.
    examples:
    - name: Deploy source code to an app. This will pack current directory, build binary with Pivotal Build Service and then deploy to the app.
      text: az spring-cloud app deploy -n MyApp -s MyCluster -g MyResourceGroup
    - name: Deploy a pre-built jar to an app with jvm options and environment variables.
      text: az spring-cloud app deploy -n MyApp -s MyCluster -g MyResourceGroup --jar-path app.jar --jvm-options="-XX:+UseG1GC -XX:+UseStringDeduplication" --env foo=bar
    - name: Deploy source code to a specific deployment of an app.
      text: az spring-cloud app deploy -n MyApp -s MyCluster -g MyResourceGroup -d green-deployment
    - name: Deploy a container image on Docker Hub to an app.
      text: az spring-cloud app deploy -n MyApp -s MyCluster -g MyResourceGroup --container-image contoso/your-app:v1
    - name: Deploy a container image on a private registry to an app.
      text: az spring-cloud app deploy -n MyApp -s MyCluster -g MyResourceGroup --container-image contoso/your-app:v1 --container-registry myacr.azurecr.io --registry-username <username> --registry-password <password>
"""

helps['spring-cloud app scale'] = """
    type: command
    short-summary: Manually scale an app or its deployments.
    examples:
    - name: Scale up an app to 4 cpu cores and 8 Gb of memory per instance.
      text: az spring-cloud app scale -n MyApp -s MyCluster -g MyResourceGroup --cpu 3 --memory 8
    - name: Scale out a deployment of the app to 5 instances.
      text: az spring-cloud app scale -n MyApp -s MyCluster -g MyResourceGroup -d green-deployment --instance-count 5
"""

helps['spring-cloud app show-deploy-log'] = """
    type: command
    short-summary: Show build log of the last deploy, only apply to source code deploy, default to production deployment.
"""

helps['spring-cloud app log tail'] = """
    type: command
    short-summary: Show logs of an app instance, logs will be streamed when setting '-f/--follow'.
"""

helps['spring-cloud app identity'] = """
    type: group
    short-summary: Manage an app's managed service identity.
"""

helps['spring-cloud app identity assign'] = """
    type: command
    short-summary: Enable managed service identity on an app.
    examples:
    - name: Enable the system assigned identity.
      text: az spring-cloud app identity assign -n MyApp -s MyCluster -g MyResourceGroup
    - name: Enable the system assigned identity on an app with the 'Reader' role.
      text: az spring-cloud app identity assign -n MyApp -s MyCluster -g MyResourceGroup --role Reader --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/xxxxx/providers/Microsoft.KeyVault/vaults/xxxxx
"""

helps['spring-cloud app identity remove'] = """
    type: command
    short-summary: Remove managed service identity from an app.
    examples:
    - name: Remove the system assigned identity from an app.
      text: az spring-cloud app identity remove -n MyApp -s MyCluster -g MyResourceGroup
"""

helps['spring-cloud app identity show'] = """
    type: command
    short-summary: Display app's managed identity info.
    examples:
    - name: Display an app's managed identity info.
      text: az spring-cloud app identity show -n MyApp -s MyCluster -g MyResourceGroup
"""

helps['spring-cloud app set-deployment'] = """
    type: command
    short-summary: Set production deployment of an app.
    examples:
    - name: Swap a staging deployment of an app to production.
      text: az spring-cloud app set-deployment -d green-deployment -n MyApp -s MyCluster -g MyResourceGroup
"""

helps['spring-cloud app unset-deployment'] = """
    type: command
    short-summary: Unset production deployment of an app.
    examples:
    - name: Swap the production deployment of an app to staging if the app has the production deployment.
      text: az spring-cloud app unset-deployment -n MyApp -s MyCluster -g MyResourceGroup
"""

helps['spring-cloud app log'] = """
    type: group
    short-summary: Commands to tail app instances logs with multiple options. If the app has only one instance, the instance name is optional.
"""

helps['spring-cloud app logs'] = """
    type: command
    short-summary: Show logs of an app instance, logs will be streamed when setting '-f/--follow'.
"""

helps['spring-cloud app deployment'] = """
    type: group
    short-summary: Commands to manage life cycle of deployments of an app in Azure Spring Cloud. More operations on deployments can be done on app level with parameter --deployment. e.g. az spring-cloud app deploy --deployment <staging deployment>
"""

helps['spring-cloud app deployment list'] = """
    type: command
    short-summary: List all deployments in an app.
"""

helps['spring-cloud app deployment show'] = """
    type: command
    short-summary: Show details of a deployment.
"""

helps['spring-cloud app deployment delete'] = """
    type: command
    short-summary: Delete a deployment of the app.
"""

helps['spring-cloud app deployment create'] = """
    type: command
    short-summary: Create a staging deployment for the app. To deploy code or update setting to an existing deployment, use `az spring-cloud app deploy/update --deployment <staging deployment>`.
    examples:
    - name: Deploy source code to a new deployment of an app. This will pack current directory, build binary with Pivotal Build Service and then deploy.
      text: az spring-cloud app deployment create -n green-deployment --app MyApp -s MyCluster -g MyResourceGroup
    - name: Deploy a pre-built jar to an app with jvm options and environment variables.
      text: az spring-cloud app deployment create -n green-deployment --app MyApp -s MyCluster -g MyResourceGroup --jar-path app.jar --jvm-options="-XX:+UseG1GC -XX:+UseStringDeduplication" --env foo=bar
    - name: Deploy a container image on Docker Hub to an app.
      text: az spring-cloud app deployment create -n green-deployment --app MyApp -s MyCluster -g MyResourceGroup --container-image contoso/your-app:v1
    - name: Deploy a container image on a private registry to an app.
      text: az spring-cloud app deployment create -n green-deployment --app MyApp -s MyCluster -g MyResourceGroup --container-image contoso/your-app:v1 --container-registry myacr.azurecr.io --registry-username <username> --registry-password <password>
"""

helps['spring-cloud app deployment generate-heap-dump'] = """
    type: command
    short-summary: Generate a heap dump of your target app instance to given file path.
"""

helps['spring-cloud app deployment generate-thread-dump'] = """
    type: command
    short-summary: Generate a thread dump of your target app instance to given file path.
"""

helps['spring-cloud app deployment start-jfr'] = """
    type: command
    short-summary: Start a JFR on your target app instance to given file path.
"""

helps['spring-cloud config-server'] = """
    type: group
    short-summary: (Support Standard Tier and Basic Tier) Commands to manage Config Server in Azure Spring Cloud.
"""

helps['spring-cloud config-server show'] = """
    type: command
    short-summary: Show Config Server.
"""

helps['spring-cloud config-server set'] = """
    type: command
    short-summary: Set Config Server from a yaml file.
"""

helps['spring-cloud config-server clear'] = """
    type: command
    short-summary: Erase all settings in Config Server.
"""

helps['spring-cloud config-server git'] = """
    type: group
    short-summary: Commands to manage Config Server git property in Azure Spring Cloud.
"""

helps['spring-cloud config-server git repo'] = """
    type: group
    short-summary: Commands to manage Config Server git repository in Azure Spring Cloud.
"""

helps['spring-cloud config-server git set'] = """
    type: command
    short-summary: Set git property of Config Server, will totally override the old one.
"""

helps['spring-cloud config-server git repo add'] = """
    type: command
    short-summary: Add a new repository of git property of Config Server.
"""

helps['spring-cloud config-server git repo remove'] = """
    type: command
    short-summary: Remove an existing repository of git property of Config Server.
"""

helps['spring-cloud config-server git repo update'] = """
    type: command
    short-summary: Override an existing repository of git property of Config Server, will totally override the old one.
"""

helps['spring-cloud config-server git repo list'] = """
    type: command
    short-summary: List all repositories of git property of Config Server.
"""

helps['spring-cloud app binding'] = """
    type: group
    short-summary: Commands to manage bindings with Azure Data Services, you need to manually restart app to make settings take effect.
"""

helps['spring-cloud app binding cosmos'] = """
    type: group
    short-summary: Commands to manage Azure Cosmos DB bindings.
"""

helps['spring-cloud app binding mysql'] = """
    type: group
    short-summary: Commands to manage Azure Database for MySQL bindings.
"""

helps['spring-cloud app binding redis'] = """
    type: group
    short-summary: Commands to manage Azure Cache for Redis bindings.
"""
helps['spring-cloud app binding list'] = """
    type: command
    short-summary: List all service bindings in an app.
"""

helps['spring-cloud app binding show'] = """
    type: command
    short-summary: Show the details of a service binding.
"""
helps['spring-cloud app binding remove'] = """
    type: command
    short-summary: Remove a service binding of the app.
"""

helps['spring-cloud app binding cosmos add'] = """
    type: command
    short-summary: Bind an Azure Cosmos DB with the app.
    examples:
    - name: Bind an Azure Cosmos DB.
      text: az spring-cloud app binding cosmos add -n cosmosProduction --app MyApp --resource-id ${COSMOSDB_ID} --api-type mongo --database mymongo -g MyResourceGroup -s MyService
"""

helps['spring-cloud app binding cosmos update'] = """
    type: command
    short-summary: Update an Azure Cosmos DB service binding of the app.
"""

helps['spring-cloud app binding mysql add'] = """
    type: command
    short-summary: Bind an Azure Database for MySQL with the app.
"""

helps['spring-cloud app binding mysql update'] = """
    type: command
    short-summary: Update an Azure Database for MySQL service binding of the app.
"""

helps['spring-cloud app binding redis add'] = """
    type: command
    short-summary: Bind an Azure Cache for Redis with the app.
"""

helps['spring-cloud app binding redis update'] = """
    type: command
    short-summary: Update an Azure Cache for Redis service binding of the app.
"""

helps['spring-cloud app append-loaded-public-certificate'] = """
    type: command
    short-summary: Append a new loaded public certificate to an app in the Azure Spring Cloud.
    examples:
    - name: Append a new loaded public certificate to an app.
      text: az spring-cloud app append-loaded-public-certificate --name MyApp --service MyCluster --resource-group MyResourceGroup --certificate-name MyCertName --load-trust-store true
"""

helps['spring-cloud certificate'] = """
    type: group
    short-summary: Commands to manage certificates.
"""

helps['spring-cloud certificate add'] = """
    type: command
    short-summary: Add a certificate in Azure Spring Cloud.
    examples:
    - name: Import certificate from key vault.
      text: az spring-cloud certificate add --name MyCertName --vault-uri MyKeyVaultUri --vault-certificate-name MyKeyVaultCertName --service MyCluster --resource-group MyResourceGroup
"""

helps['spring-cloud certificate show'] = """
    type: command
    short-summary: Show a certificate in Azure Spring Cloud.
"""

helps['spring-cloud certificate list'] = """
    type: command
    short-summary: List all certificates in Azure Spring Cloud.
    examples:
    - name: List all certificates in spring cloud service.
      text: az spring-cloud certificate list --service MyCluster --resource-group MyResourceGroup -o table
"""

helps['spring-cloud certificate remove'] = """
    type: command
    short-summary: Remove a certificate in Azure Spring Cloud.
"""

helps['spring-cloud certificate list-reference-app'] = """
    type: command
    short-summary: List all the apps reference an existing certificate in the Azure Spring Cloud.
    examples:
    - name: List all the apps reference an existing certificate in spring cloud service.
      text: az spring-cloud certificate list-reference-app --service MyCluster --resource-group MyResourceGroup --name MyCertName
"""

helps['spring-cloud app custom-domain'] = """
    type: group
    short-summary: Commands to manage custom domains.
"""

helps['spring-cloud app custom-domain bind'] = """
    type: command
    short-summary: Bind a custom domain with the app.
    examples:
    - name: Bind a custom domain to app.
      text: az spring-cloud app custom-domain bind --domain-name MyDomainName --certificate MyCertName --app MyAppName --service MyCluster --resource-group MyResourceGroup
"""

helps['spring-cloud app custom-domain show'] = """
    type: command
    short-summary: Show details of a custom domain.
"""

helps['spring-cloud app custom-domain list'] = """
    type: command
    short-summary: List all custom domains of the app.
    examples:
    - name: List all custom domains of the app.
      text: az spring-cloud app custom-domain list --app MyAppName --service MyCluster --resource-group MyResourceGroup -o table
"""

helps['spring-cloud app custom-domain update'] = """
    type: command
    short-summary: Update a custom domain of the app.
    examples:
    - name: Bind custom domain with a specified certificate.
      text: az spring-cloud app custom-domain update --domain-name MyDomainName --certificate MCertName --app MyAppName --service MyCluster --resource-group MyResourceGroup
"""

helps['spring-cloud app custom-domain unbind'] = """
    type: command
    short-summary: Unbind a custom-domain of the app.
"""

helps['spring-cloud app-insights'] = """
    type: group
    short-summary: Commands to management Application Insights in Azure Spring Cloud.
"""

helps['spring-cloud app-insights show'] = """
    type: command
    short-summary: Show Application Insights settings.
"""

helps['spring-cloud app-insights update'] = """
    type: command
    short-summary: Update Application Insights settings.
    examples:
        - name: Enable Application Insights by using the Connection string (recommended) or Instrumentation key.
          text: az spring-cloud app-insights update -n MyService -g MyResourceGroup --app-insights-key \"MyConnectionString\" --sampling-rate 100
        - name: Disable Application Insights.
          text: az spring-cloud app-insights update -n MyService -g MyResourceGroup --disable
"""

helps['spring-cloud service-registry'] = """
    type: group
    short-summary: (Support Enterprise Tier Only) Commands to manage Service Registry in Azure Spring Cloud.
"""

helps['spring-cloud service-registry show'] = """
    type: command
    short-summary: Show the provisioning status and runtime status of Service Registry.
"""

helps['spring-cloud service-registry bind'] = """
    type: command
    short-summary: Bind an app to Service Registry.
    examples:
        - name: Bind an app to Service Registry.
          text: az spring-cloud service-registry bind --app MyApp -s MyService -g MyResourceGroup
"""

helps['spring-cloud service-registry unbind'] = """
    type: command
    short-summary: Unbind an app from Service Registry.
    examples:
        - name: Unbind an app from Service Registry.
          text: az spring-cloud service-registry unbind --app MyApp -s MyService -g MyResourceGroup
"""
