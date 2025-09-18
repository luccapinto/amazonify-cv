@echo off
setlocal enabledelayedexpansion

REM Configurações
set PROJECT_NAME=amazonify-cv
set AWS_REGION=us-east-1

echo 🚀 Iniciando deploy do %PROJECT_NAME%...

REM 1. Inicializar Terraform
echo 📋 Inicializando Terraform...
cd iac
terraform init
if errorlevel 1 goto error

REM 2. Planejar infraestrutura
echo 📊 Planejando infraestrutura...
terraform plan
if errorlevel 1 goto error

REM 3. Aplicar infraestrutura
echo 🏗️ Criando infraestrutura...
terraform apply -auto-approve
if errorlevel 1 goto error

REM 4. Obter URL do ECR
echo 📦 Obtendo URL do ECR...
for /f "tokens=*" %%i in ('terraform output -raw ecr_repository_url') do set ECR_URL=%%i
echo ECR Repository: %ECR_URL%

REM 5. Fazer login no ECR
echo 🔐 Fazendo login no ECR...
for /f "tokens=*" %%i in ('aws ecr get-login-password --region %AWS_REGION%') do set ECR_PASSWORD=%%i
echo %ECR_PASSWORD% | docker login --username AWS --password-stdin %ECR_URL%
if errorlevel 1 goto error

REM 6. Construir imagem Docker
echo 🐳 Construindo imagem Docker...
cd ..
docker build -t %PROJECT_NAME% .
if errorlevel 1 goto error
docker tag %PROJECT_NAME%:latest %ECR_URL%:latest
if errorlevel 1 goto error

REM 7. Fazer push da imagem
echo 📤 Enviando imagem para ECR...
docker push %ECR_URL%:latest
if errorlevel 1 goto error

REM 8. Atualizar serviço ECS
echo 🔄 Atualizando serviço ECS...
aws ecs update-service --cluster %PROJECT_NAME% --service %PROJECT_NAME% --force-new-deployment --region %AWS_REGION%
if errorlevel 1 goto error

REM 9. Mostrar URL da aplicação
cd iac
for /f "tokens=*" %%i in ('terraform output -raw alb_url') do set ALB_URL=%%i
echo ✅ Deploy concluído!
echo 🌐 Aplicação disponível em: %ALB_URL%
echo ⏳ Aguarde alguns minutos para a aplicação ficar disponível...
goto end

:error
echo ❌ Erro durante o deploy!
exit /b 1

:end
pause