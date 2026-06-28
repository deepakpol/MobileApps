class SendPicturePrintTests:
    """Tests for HP Bridge send print jobs flow (picture and document)."""

    def test_send_picture_print_job(self):
        """
        Test sending a picture print job and verifying UI is correct.
        Covers: A picture print job can be sent and its UI is correct.
        """
        # Ensure we're at mini program home page
        self.fc.flow["hpbridge_flow"].return_home_page()
        
        # Select picture print category
        self.fc.flow["print_flow"].select_picture_print()
        
        # Select from album
        self.fc.flow["print_flow"].select_from_album()
        
        # Pick a photo (default first photo)
        self.fc.flow["print_flow"].pick_a_photo()
        
        # Verify print setting page UI
        self.fc.flow["print_setting"].verify_print_setting_page()
        
        # Click print button
        self.fc.flow["print_setting"].select_print()
        
        # Verify job submitted successfully
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()


    def test_send_document_print_job_from_wechat(self):
        """
        Test sending a document print job from WeChat.
        Covers: A document print job can be sent from WeChat.
        """
        # Launch WeChat
        self.fc.flow["hpbridge_flow"].launch_wechat()
        
        # Scan QR code to enter mini program
        self.fc.flow["wechat"].scan_qrcode_to_mp()
        
        # Select file print
        self.fc.flow["print_flow"].select_file_print()
        
        # Verify file selection options exist
        self.fc.flow["print_flow"].verify_select_options_exist(picture_print=False)
        
        # Select from chat history
        self.fc.flow["print_flow"].select_from_chat_history()
        
        # TODO: Need test data setup - select_doc_from_chat_history requires a file_name parameter but no method exists to set up or retrieve available test documents from chat history
        # self.fc.flow["print_flow"].select_doc_from_chat_history("test_document.pdf")
        
        # Verify print setting page
        self.fc.flow["print_setting"].verify_print_setting_page()
        
        # Click print button
        self.fc.flow["print_setting"].select_print()
        
        # Verify job submitted successfully
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()
