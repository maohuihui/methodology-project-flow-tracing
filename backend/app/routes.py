from flask import Blueprint, jsonify
from .models import Project

main = Blueprint('main', __name__)

@main.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@main.route('/projects', methods=['POST'])
def create_project():
    # 在这里处理项目创建逻辑
    return jsonify({'message': 'Project created!'})