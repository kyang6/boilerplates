if (self.CavalryLogger) { CavalryLogger.start_js(["iHfqu"]); }

__d("clearTimeout",["TimerStorage","TimeSliceReferenceCounting"],(function a(b,c,d,e,f,g){var h=b.clearTimeout.nativeBackup||b.clearTimeout,i=c("TimerStorage").TIMEOUT;f.exports=function(){for(var j=arguments.length,k=Array(j),l=0;l<j;l++)k[l]=arguments[l];c("TimerStorage").unset(i,k[0]);var m=i+k[0];if(k[0]!=null&&c("TimeSliceReferenceCounting").isValidCancellationToken(m))c("TimeSliceReferenceCounting").cancelTimeSlice(m);return Function.prototype.apply.call(h,b,k)}}),18);