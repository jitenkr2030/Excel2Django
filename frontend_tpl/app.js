const{createApp}=Vue;
const API='__API__';
const MODELS=__MODELS__;
createApp({
data(){return{pg:'landing',err:'',auth:!!localStorage.getItem('tk'),uname:localStorage.getItem('un')||'',user:JSON.parse(localStorage.getItem('ur')||'{}'),
lf:{u:'',p:''},rf:{u:'',e:'',p:'',fn:'',ln:'',r:'client'},
models:MODELS,cur:'',rec:{},cols:[],search:'',pn:0,ps:10,rows:[],delRec:{},
hero:'__TAG__',sub:'__SUB__',cards:['__C1__','__C2__','__C3__'],clr:'__CLR__',
roles:[{v:'creator',n:'__R1__',i:'__I1__'},{v:'client',n:'__R2__',i:'__I2__'},{v:'admin',n:'__R3__',i:'__I3__'}]}},
computed:{filtered(){if(!this.search)return this.rows;const q=this.search.toLowerCase();return this.rows.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)))},
paged(){return this.filtered.slice(this.pn*this.ps,this.pn*this.ps+this.ps)},
tp(){return Math.max(1,Math.ceil(this.filtered.length/this.ps))}},
methods:{
nav(){const h=location.hash.slice(1)||'/';this.err='';const p=h.split('/').filter(Boolean);
if(!p.length)this.pg='landing';
else if(p[0]==='login')this.pg='login';
else if(p[0]==='register')this.pg='register';
else if(p[0]==='dashboard')this.pg='dash';
else if(p[0]==='explore')this.pg='explore';
else if(p[0]==='data'&&p[1]){this.pg='data';this.cur=p[1];this.pn=0;this.load()}},
hdr(){return this.auth?{Authorization:'Token '+localStorage.getItem('tk')}:{}},
async load(){try{const r=await axios.get(API+'/api/'+this.cur.toLowerCase()+'/',{headers:this.hdr()});const d=r.data.results||r.data;this.rows=Array.isArray(d)?d:[];if(this.rows.length)this.cols=Object.keys(this.rows[0]).filter(k=>k!=='id').slice(0,8)}catch(e){this.rows=[]}},
async doLogin(){try{const r=await axios.post(API+'/api/auth/token/',{username:this.lf.u,password:this.lf.p});localStorage.setItem('tk',r.data.token);localStorage.setItem('un',this.lf.u);localStorage.setItem('ur',JSON.stringify({username:this.lf.u,role:'admin'}));this.auth=true;this.uname=this.lf.u;location.hash='/dashboard'}catch(e){this.err='Invalid credentials'}},
async doReg(){try{await axios.post(API+'/api/register/',{username:this.rf.u,email:this.rf.e,password:this.rf.p,first_name:this.rf.fn,last_name:this.rf.ln,role:this.rf.r});location.hash='/login'}catch(e){this.err=e.response?.data?.detail||'Failed'}},
logout(){localStorage.clear();this.auth=false;location.hash='/'},
async save(){try{const h=this.hdr();if(this.rec.id)await axios.put(API+'/api/'+this.cur.toLowerCase()+'/'+this.rec.id+'/',this.rec,{headers:h});else await axios.post(API+'/api/'+this.cur.toLowerCase()+'/',this.rec,{headers:h});location.hash='/data/'+this.cur}catch(e){this.err=e.response?.data?.detail||'Failed'}},
async doDel(){try{await axios.delete(API+'/api/'+this.cur.toLowerCase()+'/'+this.delRec.id+'/',{headers:this.hdr()});location.hash='/data/'+this.cur}catch(e){this.err='Failed'}}},
mounted(){this.nav();addEventListener('hashchange',this.nav)}
}).mount('#app');
