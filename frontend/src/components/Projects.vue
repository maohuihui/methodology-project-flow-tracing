
<template>
  <div>
    <h1>项目列表</h1>
    <ul>
      <li v-for="project in projects" :key="project.id">
        {{ project.name }} - {{ project.project_type }} - {{ project.duration }} 天
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      projects: []
    };
  },
  created() {
    axios.get('http://localhost:5000/projects')
      .then(response => {
        this.projects = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
