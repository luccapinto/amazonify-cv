#!/bin/bash

set -e

# Configurações
PROJECT_NAME="amazonify-cv"
AWS_REGION="us-east-1"

echo "🚀 Iniciando deploy do $PROJECT_NAME..."

# 1. Inicializar Terraform
echo "📋 Inicializando Terraform..."
cd iac
terraform init

# 2. Planejar infraestrutura
echo "📊 Planejando infraestrutura..."
terraform plan

# 3. Aplicar infraestrutura
echo "🏗️ Criando infraestrutura..."
terraform apply -auto-approve

# 4. Obter URL do ECR
ECR_URL=$(terraform output -raw ecr_repository_url)
echo "📦 ECR Repository: $ECR_URL"

# 5. Fazer login no ECR
echo "🔐 Fazendo login no ECR..."
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URL

# 6. Construir imagem Docker
echo "🐳 Construindo imagem Docker..."
cd ..
docker build -t $PROJECT_NAME .
docker tag $PROJECT_NAME:latest $ECR_URL:latest

# 7. Fazer push da imagem
echo "📤 Enviando imagem para ECR..."
docker push $ECR_URL:latest

# 8. Atualizar serviço ECS
echo "🔄 Atualizando serviço ECS..."
aws ecs update-service --cluster $PROJECT_NAME --service $PROJECT_NAME --force-new-deployment --region $AWS_REGION

# 9. Mostrar URL da aplicação
cd iac
ALB_URL=$(terraform output -raw alb_url)
echo "✅ Deploy concluído!"
echo "🌐 Aplicação disponível em: $ALB_URL"
echo "⏳ Aguarde alguns minutos para a aplicação ficar disponível..."