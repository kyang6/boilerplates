if (self.CavalryLogger) { CavalryLogger.start_js(["Pl\/e7"]); }

__d("EmbeddedVideoCastingControl.react",["cx","ix","fbt","AbstractButton.react","Image.react","React"],(function a(b,c,d,e,f,g,h,i,j){"use strict";var k,l,m=c("React").PropTypes;k=babelHelpers.inherits(n,c("React").PureComponent);l=k&&k.prototype;function n(){var o,p;for(var q=arguments.length,r=Array(q),s=0;s<q;s++)r[s]=arguments[s];return p=(o=l.constructor).call.apply(o,[this].concat(r)),this.onButtonClick=function(){var t=this.props.isCasting?this.props.onStopCast:this.props.onStartCast;if(t)t()}.bind(this),p}n.prototype.render=function(){var o=this.props.isCasting?i("101646"):i("101647"),p=c("React").createElement(c("Image.react"),{className:"_5i0o",src:o});return c("React").createElement(c("AbstractButton.react"),{className:"_3u33",image:p,label:j._("Cast to Chrome Cast"),labelIsHidden:true,onClick:this.onButtonClick,ref:"button",tabIndex:this.props.tabIndex,type:"button"})};n.propTypes={hasFoundReceiver:m.bool,isCasting:m.bool,isCastingSupported:m.bool,onStartCast:m.func,onStopCast:m.func,tabIndex:m.string};f.exports=n}),null);