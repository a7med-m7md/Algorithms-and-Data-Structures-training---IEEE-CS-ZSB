static long largestRectangle(int [] h) {
int i,j,count,min;
int Area,Max=0;
int n=h.length;
h[n]=0;            
for(i=0;i<n;i++){
  count=1;        
  min=h[i];
  j=i-1;
  while(j>=0){   
    if(h[j]>min){      
      count++;
      j--;
    }
    else 
    break;
  }
  while(h[i+1]==min&&i+1<n){  
    i++;    
    count++;
  }  
  j=i+1;
  while(h[j]>=min&&j<n){    
    j++;      
    count++;
  }
  Area=min*count;
  if(Area>Max)
    Max=Area;
}
return Max;
}
