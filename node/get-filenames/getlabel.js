const treeData = [{
  title: '服务器',
  value: '0-0',
  key: '0-0',
  children: [{
    title: '应用服务器',
    value: '0-0-1',
    key: '0-0-1',
  }, {
    title: '数据服务器',
    value: '0-0-2',
    key: '0-0-2',
  }],
}, {
  title: '网路设备',
  value: '0-1',
  key: '0-1',
  children: [{
    title: '路由器',
    value: '0-1-1',
    key: '0-1-1',
  }, {
    title: '交换机',
    value: '0-1-2',
    key: '0-1-2',
  }, {
    title: '负载均衡',
    value: '0-1-3',
    key: '0-1-3',
  }],
}, {
  title: '安全设备',
  value: '0-2',
  key: '0-2',
  children: [{
    title: '防火墙',
    value: '0-2-1',
    key: '0-2-1',
  }, {
    title: 'IPS',
    value: '0-2-2',
    key: '0-2-2',
  }, {
    title: 'IDS',
    value: '0-2-3',
    key: '0-2-3',
  }, {
    title: '堡垒机',
    value: '0-2-4',
    key: '0-2-4',
  }],
}];

function renderTreeTitle(props) {
  const { value } = props
  let title = '-'
  if (value) {
    const getTitle = (parent, key) => {
      for (let index = 0; index < parent.length; index++) {
        const element = parent[index];
        if (element.value === key) {
          title = element.title;
          break;
        } else {
          if (element.children) {
            getTitle(element.children, key)
          }
        }
      }
    }
    getTitle(treeData, value)
  }
  return title
}

const aa = renderTreeTitle(treeData)
console.log(aa, 'aa')