pipeline {

    agent any

    environment {
        COMPOSE_PROJECT_NAME = "fullstack-app"
    }

    stages {

        // ========================
        // 1. 소스 준비 (전체 clone 기준)
        // ========================
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // ========================
        // 2. React 의존성 설치 (옵션 - Docker build로 대체 가능)
        // ========================
        stage('Install Frontend Dependencies') {
            steps {
                sh '''
                    cd frontend
                    npm ci
                '''
            }
        }

        // ========================
        // 3. React 빌드
        // ========================
        stage('Build React') {
            steps {
                sh '''
                    cd frontend
                    npm run build
                '''
            }
        }

        // ========================
        // 4. Django 준비 (migrate 체크용)
        // ========================
        stage('Backend Check') {
            steps {
                sh '''
                    cd backend
                    echo "Backend ready"
                '''
            }
        }

        // ========================
        // 5. Docker Build (전체)
        // ========================
        stage('Docker Build') {
            steps {
                sh '''
                    docker compose build
                '''
            }
        }

        // ========================
        // 6. DB 포함 전체 배포
        // ========================
        stage('Deploy') {
            steps {
                sh '''
                    docker compose down || true
                    docker compose up -d
                '''
            }
        }

        // ========================
        // 7. DB Migration (중요)
        // ========================
        stage('Run Django Migration') {
            steps {
                sh '''
                    docker compose exec -T backend python manage.py migrate
                '''
            }
        }

    }

    post {

        success {
            echo '🚀 전체 (React + Django + Postgres + Nginx) 배포 완료'
        }

        failure {
            echo '❌ 배포 실패'
        }

        always {
            echo 'Pipeline 종료'
        }
    }
}