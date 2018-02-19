package io.netty.restapi;

import com.google.gson.JsonObject;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Map;

/**
 * Created by SunMyeong Lee on 2016-08-31.
 */
public abstract class ApiRequestTemplate implements ApiRequest {
    protected Logger logger;

    protected Map<String, String> reqData;

    protected JsonObject apiResult;

    public ApiRequestTemplate(Map<String, String> reqData) {
        this.logger = LogManager.getLogger(this.getClass());
        this.apiResult = new JsonObject();
        this.reqData = reqData;

        logger.info("request data : " + this.reqData);
    }



    @Override
    public void executeService() {
        try {
            this.requestParamValidation();

            this.service();
        }
        catch (ServiceException e) {
            logger.error(e);
            this.apiResult.addProperty("resultCode", "405");
        } catch (RequestParamException e) {
            logger.error(e);
            this.apiResult.addProperty("resultCode", "501");
        }
    }

    @Override
    public JsonObject getApiResult() {
        return this.apiResult;
    }
}
