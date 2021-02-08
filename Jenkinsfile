#!/usr/bin/env groovy

//adapted from https://www.christopherrung.com/2017/05/04/slack-build-notifications/

import groovy.json.JsonOutput
//import java.util.Optional
//import hudson.tasks.test.AbstractTestResultAction
//import hudson.model.Actionable
//import hudson.tasks.junit.CaseResult

def slackNotificationChannel = "jenkins_test"     

def notifySlack(text, channel, attachments) {
    
    def slackURL = sh(returnStdout: true, script: 'less /usr/local/var/homebrew/linked/jenkins-lts/codingjuntos_advent2020/my_webhook_test').trim()

    def jenkinsIcon = 'https://wiki.jenkins-ci.org/download/attachments/2916393/logo.png'

    def payload = JsonOutput.toJson([text: text,
        channel: channel,
        username: "Jenkins",
        icon_url: jenkinsIcon,
        attachments: attachments
    ])

    sh "curl -X POST --data-urlencode \'payload=${payload}\' ${slackURL}"
}


node {
    
    stage("Post to Slack") {
        
        sh 'echo hello'
        sh 'python /usr/local/var/homebrew/linked/jenkins-lts/codingjuntos_advent2020/some_test.py &> out.txt '     
 
        def testSummary = sh(returnStdout: true, script:'less out.txt').trim()        
 
        notifySlack("", slackNotificationChannel, [
           [
              title: "${env.JOB_NAME}, build #${env.BUILD_NUMBER}",
              text: "hello",
              color: "#0339fc",
              fields:[
                 [
                    title: "Test Results",
                    value: "${testSummary}",
                    short: true 
                 ]
              ]
           ]
        ])

    }
        sh 'echo hello'
}

